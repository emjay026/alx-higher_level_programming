#!/usr/bin/python3
"""Python script that fetches a resource
"""
if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    if response.status_code == 200:
        content_type = type(response.text)
        content = response.text
        print("Body response:")
        print(f"\t- type: {content_type}")
        print(f"\t- content: {content}")
