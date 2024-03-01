#!/usr/bin/python3
"""Python script that fetches a resource
"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    request_id = response.headers.get('X-Request-Id')
    if request_id:
        print(f"{request_id}")
