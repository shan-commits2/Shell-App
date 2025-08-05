import psutil

def main(args):
    print("[*] Disk usage info:\n")
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"{partition.device}: {usage.used // (1024**3)} GB used / {usage.total // (1024**3)} GB total ({usage.percent}%)")
        except:
            continue
