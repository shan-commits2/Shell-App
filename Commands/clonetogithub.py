import os
import subprocess
import shutil

def is_git_available():
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def try_find_git_in_common_paths():
    possible_paths = [
        r"C:\Program Files\Git\cmd\git.exe",
        r"C:\Program Files (x86)\Git\cmd\git.exe",
        r"C:\Program Files\Git\bin\git.exe",
        r"C:\Program Files (x86)\Git\bin\git.exe"
    ]
    for path in possible_paths:
        if os.path.isfile(path):
            return path
    return None

def main(args):
    if not args:
        print("[!] Usage: githubclone [https://github.com/user/repo.git]")
        return

    repo_url = args[0]
    print("[*] Checking Git installation...")

    git_cmd = "git"
    if not is_git_available():
        found_git = try_find_git_in_common_paths()
        if found_git:
            git_cmd = found_git
            print(f"[✓] Found Git at: {found_git}")
        else:
            print("[!] Git is not installed or not found in PATH.")
            return

    print("[*] Initializing Git repository...")
    try:
        if not os.path.isdir(".git"):
            subprocess.run([git_cmd, "init"], check=True)
    except subprocess.CalledProcessError:
        print("[!] Failed to initialize Git repository.")
        return

    print("[*] Adding all files...")
    subprocess.run([git_cmd, "add", "."], check=False)

    if not os.path.exists(".gitignore"):
        with open(".gitignore", "w") as f:
            f.write(".DS_Store\n__pycache__/\n*.pyc\n.env\nnode_modules/\n")

    print("[*] Creating commit...")
    subprocess.run([git_cmd, "commit", "-m", "Initial upload via githubclone"], check=False)

    print("[*] Configuring remote origin...")
    remotes = subprocess.run([git_cmd, "remote"], capture_output=True, text=True)
    if "origin" in remotes.stdout:
        subprocess.run([git_cmd, "remote", "remove", "origin"], check=False)
    subprocess.run([git_cmd, "remote", "add", "origin", repo_url], check=False)

    print("[*] Pushing to GitHub...")
    try:
        subprocess.run([git_cmd, "branch", "-M", "main"], check=True)
        subprocess.run([git_cmd, "push", "-u", "origin", "main"], check=True)
        print("[✓] Successfully pushed to GitHub!")
    except subprocess.CalledProcessError as e:
        print("[!] Initial push failed.")
        print("    Trying to force push (overwrite remote)...")
        try:
            subprocess.run([git_cmd, "push", "-f", "-u", "origin", "main"], check=True)
            print("[✓] Successfully force-pushed to GitHub!")
        except subprocess.CalledProcessError as e2:
            print("[X] Force push also failed.")
            print("    Make sure the GitHub repo exists and credentials are configured.")
            print(f"    Error: {e2}")
