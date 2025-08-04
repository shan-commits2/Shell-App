import subprocess, os, sys, shutil

def main(args):
    if not args:
        print("[!] Usage: runjs [file.js]")
        return
    file = args[0]
    if not os.path.isfile(file):
        print("[!] File not found")
        return

    node_path = shutil.which("node")
    if not node_path:
        print("[*] Node.js not found. Attempting to install...")
        try:
            if sys.platform.startswith("win"):
                subprocess.run(["winget", "install", "-e", "--id", "OpenJS.NodeJS"], check=True)
            elif sys.platform.startswith("linux"):
                subprocess.run(["sudo", "apt", "install", "-y", "nodejs", "npm"], check=True)
            elif sys.platform == "darwin":
                subprocess.run(["brew", "install", "node"], check=True)
            else:
                print("[!] Unknown OS. Install Node.js manually.")
                return
        except Exception as e:
            print("[!] Failed to install Node.js:", e)
            return

    subprocess.run(["node", file])
