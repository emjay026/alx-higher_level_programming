#!/usr/bin/python3
"""Python script that fetches a resource
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    if request_id:
        print(request_id)
