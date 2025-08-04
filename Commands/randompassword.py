import string
import secrets
import sys

def main(args):
    import argparse

    parser = argparse.ArgumentParser(description="Strong Password Generator")
    parser.add_argument("length", type=int, nargs='?', default=16, help="Password length (default: 16)")
    parser.add_argument("--nosymbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--noambiguous", action="store_true", help="Exclude ambiguous characters like 0, O, l, 1, I")
    parser.add_argument("--include", type=str, help="Force include specific characters")
    parser.add_argument("--exclude", type=str, help="Exclude specific characters")
    parser.add_argument("--count", type=int, default=1, help="Generate multiple passwords")
    args = parser.parse_args(args)

    if args.length < 8:
        print("[!] Password length should be at least 8 for strong security")
        return

    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    chars = lower + upper + digits
    if not args.nosymbols:
        chars += symbols

    # Remove ambiguous characters
    if args.noambiguous:
        for c in "O0Il1":
            chars = chars.replace(c, '')

    # Exclude user-defined
    if args.exclude:
        for c in args.exclude:
            chars = chars.replace(c, '')

    if not chars:
        print("[!] No characters left to generate password. Check your filters.")
        return

    # Password generation
    for i in range(args.count):
        password = ''.join(secrets.choice(chars) for _ in range(args.length))
        if args.include:
            forced = ''.join(secrets.choice(args.include) for _ in range(min(len(args.include), args.length)))
            password = list(password)
            for i in range(len(forced)):
                password[i] = forced[i]
            secrets.SystemRandom().shuffle(password)
            password = ''.join(password)

        print(f"[✓] Password {i+1}: {password}")

    print("\n[✔] Tip: Use a password manager to store your passwords securely.")
    print("[✔] Symbols make passwords harder to crack. Avoid dictionary-based words.")

