import json, yaml

def main(args):
    if len(args) != 2:
        print("[!] Usage: convert [file1.json/yaml] [file2.yaml/json]")
        return

    file1, file2 = args
    try:
        with open(file1, 'r') as f:
            if file1.endswith(".json") and file2.endswith(".yaml"):
                data = json.load(f)
                with open(file2, 'w') as out:
                    yaml.dump(data, out)
                print("[✓] Converted JSON to YAML")
            elif file1.endswith(".yaml") and file2.endswith(".json"):
                data = yaml.safe_load(f)
                with open(file2, 'w') as out:
                    json.dump(data, out, indent=2)
                print("[✓] Converted YAML to JSON")
            else:
                print("[!] Unsupported file types")
    except Exception as e:
        print("[!] Conversion failed:", e)
