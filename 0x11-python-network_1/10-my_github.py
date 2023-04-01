#!/usr/bin/python3
"""Uses the GitHub API to display a"""
import requests
from requests.auth import HTTPBasicAuth
import sys



if __name__ == "__main__":
    autho = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=autho)
    print(r.json().get("id"))
