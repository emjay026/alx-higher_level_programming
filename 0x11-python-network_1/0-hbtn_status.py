#!/usr/bin/python3
"""Python script that fetches a resource
"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    data = response.read()
    content_type = type(data)
    utf8_content = data.decode('utf-8')

print("Body response:")
print(f"\t- type: {content_type}")
print(f"\t- content: {data}")
print(f"\t- utf8 content: {utf8_content}")
