import os

def main(args):
    if not args:
        print("[!] Usage: read [filename]")
        return
    file = args[0]
    if not os.path.isfile(file):
        print("[!] File not found")
        return
    try:
        with open(file, 'r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e:
        print("[!] Error reading file:", e)
