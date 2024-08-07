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
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        content = response.text.strip()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

if __name__ == '__main__':
    # URLs to fetch from
    urls = [
        'https://intranet.hbtn.io/status',
        'http://0.0.0.0:5050/status'
    ]
    
    for url in urls:
        print(f"Fetching status from: {url}")
        fetch_status(url)
        print()
