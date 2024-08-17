#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""


import requests


"""
def number_of_subscribers(subreddit):
Return the total number of subscribers on a given subreddit.
url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers, allow_redirects=False)
if response.status_code == 200:
data = response.json()
subscribers = data['data']['subscribers']
return subscribers
else:
return 0"""


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a
    given subreddit.
    If the subreddit is invalid, it returns 0.

    :param subreddit: The name of the subreddit to query.
    :return: The number of subscribers or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-reddit-script/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0
