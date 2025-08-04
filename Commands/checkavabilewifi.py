import subprocess
import os
import re

def get_saved_wifi_profiles():
    try:
        output = subprocess.check_output("netsh wlan show profiles", shell=True, text=True, stderr=subprocess.DEVNULL)
        return re.findall(r"All User Profile\s*:\s(.*)", output)
    except:
        return []

def get_wifi_password(profile_name):
    try:
        command = f'netsh wlan show profile name="{profile_name}" key=clear'
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.DEVNULL)
        match = re.search(r"Key Content\s*:\s(.*)", output)
        return match.group(1) if match else "NO PASSWORD FOUND"
    except:
        return "ERROR FETCHING"

def get_signal_strength():
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True, text=True, stderr=subprocess.DEVNULL)
        match = re.search(r"^\s*Signal\s*:\s*(\d+)%", output, re.MULTILINE)
        if match:
            signal = int(match.group(1))
            if signal >= 80:
                return f"{signal}% (Strong)"
            elif signal >= 40:
                return f"{signal}% (Medium)"
            else:
                return f"{signal}% (Weak)"
        return "Not Connected"
    except:
        return "Error"

def main(args):
    if os.name != 'nt':
        print("This command only works on Windows (netsh is Windows-only).")
        return

    print("[*] Fetching saved Wi-Fi profiles...\n")

    profiles = get_saved_wifi_profiles()
    if not profiles:
        print("No saved Wi-Fi profiles found.")
        return

    current_signal = get_signal_strength()

    for profile in profiles:
        profile = profile.strip().strip('"')
        password = get_wifi_password(profile)
        print(f"📶 {profile}")
        print(f"    🔑 Password   : {password}")
        print(f"    📡 Strength   : {current_signal}\n")
