import subprocess
import re

def main(args):
    print("[*] Scanning nearby Wi-Fi networks...\n")

    try:
        result = subprocess.run(["netsh", "wlan", "show", "networks", "mode=bssid"],
                                capture_output=True, text=True, check=True)
    except Exception as e:
        print(f"[!] Failed to scan networks: {e}")
        return

    output = result.stdout
    networks = re.split(r'\n\s*\n', output)

    for block in networks:
        ssid_match = re.search(r'SSID\s+\d+\s+:\s(.+)', block)
        signal_match = re.search(r'Signal\s+:\s+(\d+)%', block)
        auth_match = re.search(r'Authentication\s+:\s+(.+)', block)

        if ssid_match and signal_match:
            ssid = ssid_match.group(1)
            signal = int(signal_match.group(1))
            bars = get_signal_bars(signal)
            auth = auth_match.group(1) if auth_match else "Unknown"
            print(f"📶 {ssid}  ({signal}%) {bars}  🔒 {auth}")
    
def get_signal_bars(signal):
    if signal >= 80:
        return "🟩🟩🟩🟩"
    elif signal >= 60:
        return "🟩🟩🟩⬜"
    elif signal >= 40:
        return "🟩🟩⬜⬜"
    elif signal >= 20:
        return "🟩⬜⬜⬜"
    else:
        return "⬜⬜⬜⬜"
