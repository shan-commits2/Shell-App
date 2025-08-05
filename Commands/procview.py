import psutil

def main(args):
    print("[*] Listing running processes...\n")
    print("{:<6} {:<25} {:<8} {:<10}".format("PID", "Name", "CPU %", "RAM MB"))

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            mem_mb = proc.info['memory_info'].rss / (1024 * 1024)
            print("{:<6} {:<25} {:<8} {:<10.2f}".format(
                proc.info['pid'], proc.info['name'], proc.info['cpu_percent'], mem_mb))
        except:
            continue
