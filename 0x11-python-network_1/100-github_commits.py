#!/usr/bin/python3
"""Python script that fetches a resource
"""
if __name__ == "__main__":
    import requests
    import sys

    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    response = requests.get(url)

    def sort_key(commit):
        return commit['commit']['committer']['date']

    if response.status_code == 200:
        user_data = response.json()
        sorted_commits = sorted(user_data, key=sort_key)
        count = 10
        for commit in sorted_commits:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
            count -= 1
            if count == 0:
                break
