#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers (not active users,
 total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:\
v1.0.0 (by /u/aaorrico23)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
