import os
import shutil

def main(args):
    temp_paths = [os.getenv('TEMP'), os.getenv('TMP'), r"C:\Windows\Temp"]
    deleted = 0

    print("[*] Cleaning temp folders...\n")

    for temp in temp_paths:
        if not temp or not os.path.exists(temp): continue
        for root, dirs, files in os.walk(temp):
            for file in files:
                path = os.path.join(root, file)
                try:
                    os.remove(path)
                    deleted += 1
                except: pass
            for dir in dirs:
                path = os.path.join(root, dir)
                try:
                    shutil.rmtree(path, ignore_errors=True)
                    deleted += 1
                except: pass

    print(f"[✓] Cleanup complete. Deleted {deleted} files/folders.")
