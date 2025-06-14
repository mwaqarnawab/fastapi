# app.py
import sys
import json

def main():
    payload_file = sys.argv[1]
    with open(payload_file, 'r') as f:
        payload = json.load(f)

    # Access parameters
    param1 = payload.get("param1", "default1")
    param2 = payload.get("param2", "default2")

    print(f"Received param1: {param1}")
    print(f"Received param2: {param2}")

if __name__ == "__main__":
    main()
