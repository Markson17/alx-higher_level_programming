#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import sys
import requests


if __name__ == "__main__":
    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(req.text)
