import subprocess, sys

def main(args):
    if not args:
        print("[!] Usage: pipinstall [package]")
        return
    package = args[0]
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"[+] Successfully installed: {package}")
    except subprocess.CalledProcessError:
        print(f"[!] Failed to install package: {package}")
