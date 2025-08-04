import subprocess, os, sys

def main(args):
    if not args:
        print("[!] Usage: run [filename.py]")
        return
    file = args[0]
    if not os.path.isfile(file):
        print("[!] File not found")
        return
    subprocess.run([sys.executable, file])
