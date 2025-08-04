import subprocess, os, sys, shutil

def main(args):
    if not args:
        print("[!] Usage: runlua [file.lua]")
        return
    file = args[0]
    if not os.path.isfile(file):
        print("[!] File not found")
        return

    lua_path = shutil.which("lua")
    if not lua_path:
        print("[*] Lua not found. Attempting to install...")
        try:
            if sys.platform.startswith("win"):
                subprocess.run(["winget", "install", "-e", "--id", "Lua.Lua"], check=True)
            elif sys.platform.startswith("linux"):
                subprocess.run(["sudo", "apt", "install", "-y", "lua5.4"], check=True)
            elif sys.platform == "darwin":
                subprocess.run(["brew", "install", "lua"], check=True)
            else:
                print("[!] Unknown OS. Install Lua manually.")
                return
        except Exception as e:
            print("[!] Failed to install Lua:", e)
            return

    subprocess.run(["lua", file])
