import os

def main(args):
    directory = args[0] if args else "."
    print(f"[+] Scanning largest files in: {directory}\n")

    files = []
    for root, _, filenames in os.walk(directory):
        for file in filenames:
            path = os.path.join(root, file)
            try:
                size = os.path.getsize(path)
                files.append((path, size))
            except:
                continue

    files.sort(key=lambda x: x[1], reverse=True)
    top = files[:10]

    for path, size in top:
        print(f"{size / (1024 * 1024):.2f} MB  →  {path}")
