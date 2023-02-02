#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0)\
     Gecko/20100101 Firefox/57.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            print(response.json().get("data").get("children")[i].get("data")
                  .get("title"))
    else:
        print("None")
