import psutil

def main(args):
    print("[*] Scanning running processes...\n")
    sus_keywords = ["keylogger", "rat", "stealer", "mimikatz", "unknown", "hack", "inject"]

    flagged = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pname = proc.info['name'].lower()
            if any(k in pname for k in sus_keywords):
                flagged.append(proc.info)
        except:
            continue

    if not flagged:
        print("[✓] No suspicious processes found.")
    else:
        print("[!] Suspicious processes:")
        for proc in flagged:
            print(f"⚠️  {proc['name']} (PID: {proc['pid']})")
