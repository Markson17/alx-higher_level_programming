#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status and givs error message"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html_code = response.read()
            print(html_code.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
