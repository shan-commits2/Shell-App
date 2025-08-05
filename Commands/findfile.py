import os
from pathlib import Path

def main(args):
    if not args:
        print("[!] Usage: findfile [filename]")
        return

    filename = args[0].lower()
    found = []
    print(f"[*] Searching for '{filename}'...\n")

    for root, dirs, files in os.walk(Path.home().drive + "\\"):
        for file in files:
            if file.lower() == filename:
                path = os.path.join(root, file)
                print(f"[✓] Found: {path}")
                found.append(path)

    if not found:
        print("[✗] File not found.")
