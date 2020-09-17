#!/usr/bin/python3
"""requests api """
import requests


def top_ten(subreddit):
    """ api reddit """
    r = requests.get("https://reddit.com/r/{}.json?sort=hot&limit=10".
                     format(subreddit), headers={"User-agent": "custom"})

    if(r.status_code == 200):
        for subred in r.json().get("data").get("children"):
            print(subred.get("data").get("title"))
    else:
        print("None")
