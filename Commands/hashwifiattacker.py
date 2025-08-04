import subprocess
import os

def main(args):
    if len(args) < 3:
        print("Usage: CrackHash [hash_file] [wordlist] [hash_mode] [optional: attack_mode (default 0)]")
        return

    hash_file = args[0]
    wordlist = args[1]
    hash_mode = args[2]
    attack_mode = args[3] if len(args) > 3 else "0"  # Default to dictionary attack

    if not os.path.exists(hash_file):
        print(f"[!] Hash file not found: {hash_file}")
        return
    if not os.path.exists(wordlist):
        print(f"[!] Wordlist not found: {wordlist}")
        return

    print(f"[*] Cracking hash with mode={attack_mode}, type={hash_mode}...\n")

    command = [
        "hashcat",
        "-a", attack_mode,
        "-m", hash_mode,
        hash_file,
        wordlist,
        "--force",          # Forces CPU fallback if GPU errors
        "--status",         # Shows live status
        "--potfile-disable" # Don't save cracked passwords to disk
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Hashcat error:\n{e}")

    print("\n[*] Done. If password was found, it should be shown above.")
