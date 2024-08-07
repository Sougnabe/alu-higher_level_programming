#!/usr/bin/python3
"""
A Python script that fetches https://alu-intranet.hbtn.io/status.
"""

import requests

def fetch_status(url):
    """
documented
    """
    response = requests.get(url)
    content = response.text.strip()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

if __name__ == '__main__':
    fetch_status('http://0.0.0.0:5050/status')
    fetch_status('https://intranet.hbtn.io/status')
