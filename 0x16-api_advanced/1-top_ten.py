#!/usr/bin/python3
"""File Doc"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot
    posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}
    headers = {"User-Agent": "0x16-api_advanced/V1"}
    response = requests.get(url, headers=headers, allow_redirects=False, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)
