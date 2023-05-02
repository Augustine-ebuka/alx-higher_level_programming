#!/usr/bin/python3
"""
- Python script that takes in a URL
- sends a request to the URL and
- displays the value of the X-Request-Id variable
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.openurl(req) as respond:
        print(dict(respond.headers).get('X-Request-Id')
