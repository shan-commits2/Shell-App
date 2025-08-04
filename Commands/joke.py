"""
Get a random programming joke.
Usage: joke
"""

import requests

def main(args):
    url = "https://v2.jokeapi.dev/joke/Programming?type=single"
    try:
        resp = requests.get(url, timeout=5)
        data = resp.json()
        if resp.status_code == 200 and "joke" in data:
            print(f"\n😂 {data['joke']}\n")
        else:
            print("[!] Couldn't fetch a joke right now.")
    except Exception as e:
        print(f"[!] Error getting joke: {e}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])