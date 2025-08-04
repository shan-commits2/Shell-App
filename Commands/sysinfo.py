import platform
import psutil
import time

def main(args):
    print("[*] Gathering system info...\n")
    print(f"🖥️  OS          : {platform.platform()}")
    print(f"🧠 CPU         : {platform.processor()}")
    print(f"🧩 Cores       : {psutil.cpu_count(logical=False)}")
    print(f"🔁 Threads     : {psutil.cpu_count(logical=True)}")
    print(f"💾 RAM         : {round(psutil.virtual_memory().total / 1024**3, 2)} GB")
    print(f"📊 RAM Usage   : {psutil.virtual_memory().percent}%")
    print(f"💽 Disk Usage  : {psutil.disk_usage('/').percent}%")
    uptime = round((time.time() - psutil.boot_time()) / 3600, 2)
    print(f"⏱️  Uptime      : {uptime} hours")
