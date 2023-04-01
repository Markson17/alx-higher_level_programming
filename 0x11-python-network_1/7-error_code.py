#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    try:
        req.raise_for_status()
        print(req.text)
    except Exception as e:
        print("Error code: {}".format(req.status_code))
