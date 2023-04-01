#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import sys
import requests


if __name__ == "__main__":
    x = ""
    if len(sys.argv) > 1:
        x = sys.argv[1]
    args = requests.post('http://0.0.0.0:5000/search_user', data={'q': x})
    try:
        args.raise_for_status()
        json = args.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(json['id'], json['name']))
    except Exception:
        print("Not a valid JSON")
