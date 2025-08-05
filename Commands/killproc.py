import psutil

def main(args):
    if not args:
        print("[!] Usage: kill [pid or process name]")
        return

    target = args[0]
    if target.isdigit():
        pid = int(target)
        try:
            psutil.Process(pid).terminate()
            print(f"[✓] Killed process with PID {pid}")
        except Exception as e:
            print(f"[!] Failed to kill PID {pid}: {e}")
    else:
        killed = []
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'].lower() == target.lower():
                try:
                    proc.terminate()
                    killed.append(proc.info['pid'])
                except Exception as e:
                    print(f"[!] Error terminating: {e}")
        if killed:
            print(f"[✓] Killed processes: {killed}")
        else:
            print("[!] No matching process found.")
