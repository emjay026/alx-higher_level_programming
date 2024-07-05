#!/usr/bin/python3
"""Python script that fetches a resource
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')

    print(f"{request_id}")
