#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests

req = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
