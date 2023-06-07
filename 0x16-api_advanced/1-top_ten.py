#!/usr/bin/python3
"a function that queries the Reddit API and prints the titles of the first 10 hot posts"

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url,
                       headers={'user-agent': 'Mozilla/5.0'},
                       params={'limit': '10'},
                       allow_redirects=False)
    if req.status_code != 200:
        print(None)
    else:
        json_req = req.json()
        for post in json_req["data"]["children"]:
            print(post["data"]["title"])
