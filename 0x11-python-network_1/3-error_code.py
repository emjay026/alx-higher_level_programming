#!/usr/bin/python3
"""Python script that fetches a resource
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
