#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.)
"""

import requests


def count_words(subreddit, word_list, after=None):
    """recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.)
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
               }
    params = {'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    data = data.get('data')
    children = data.get('children')
    for child in children:
        title = child.get('data').get('title')
        for word in word_list:
            if word.lower() in title.lower():
                print(word)
    after = data.get('after')
    if after is None:
        return None
    return count_words(subreddit, word_list, after)
