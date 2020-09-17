#!/usr/bin/python3
"""2 recurse """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries the API and returns a list containing the titles"""

    url = 'http://reddit.com/r/{}/hot.json?after={}'
    headers = {'User-agent': 'custom'}
    response = requests.get(url.format(subreddit, after),
                            headers=headers)
    if response.status_code == 200:
        first_posts = response.json()
        key = first_posts['data']['after']
        parent = first_posts['data']['children']
        for obj in parent:
            hot_list.append(obj['data']['title'])
        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    else:
        return None
