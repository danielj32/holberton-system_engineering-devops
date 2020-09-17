#!/usr/bin/python3
"""requests api """
import requests


def number_of_subscribers(subreddit):
    """ api reddit """
    url = 'http://reddit.com/r/{}/about.json'
    headers = {'User-agent': 'custom'}
    r = requests.get(url.format(subreddit), headers=headers)
    if(r.status_code == 200):
        count = r.json().get("data").get("subscribers")
        return count
    else:
        return 0
