#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import sys
from urllib import request



if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        print(res.getheader("X-Request-Id"))
