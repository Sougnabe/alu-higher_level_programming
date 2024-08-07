#!/usr/bin/python3
"""
A Python script that fetches a status from a specified URL.
"""

import requests

def fetch_status(url):
    """
    Fetches the status from a given URL and prints the response details.
    
    Args:
        url (str): The URL to fetch the status from.
    
    Returns:
        None
    """
    response = requests.get(url)
    content = response.text.strip()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

if __name__ == '__main__':
    urls = [
        'https://intranet.hbtn.io/status',
        'http://0.0.0.0:5050/status'
    ]
    
    for url in urls:
        print(f"Fetching status from: {url}")
        fetch_status(url)
        print()
