#!/usr/bin/python3
"""Python script that fetches a resource
"""
if __name__ == "__main__":
    import requests
    import sys

    letter = ""

    if len(sys.argv) == 2:
        letter = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
