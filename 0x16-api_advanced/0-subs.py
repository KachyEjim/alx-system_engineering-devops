#!/usr/bin/python3
"""FILE DOC"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns
    the number of subscribers for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "0x16-api_advanced/V1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    return 0
