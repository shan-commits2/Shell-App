import uuid, secrets

def main(args):
    secret_type = args[0] if len(args) > 0 else "uuid"
    length = int(args[1]) if len(args) > 1 else 32

    if secret_type == "uuid":
        print(str(uuid.uuid4()))
    elif secret_type == "hex":
        print(secrets.token_hex(length // 2))
    elif secret_type == "token":
        print(secrets.token_urlsafe(length))
    else:
        print("[!] Unknown type. Use: uuid, hex, token")
