#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ function to get # of subscribers """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {
        'User-agent': 'Mozilla/5.0'
    }
    res = requests.get(url, headers=header)
    if res.status_code is 200:
        res = res.json()
        return res.get('data').get('subscribers')
    else:
        return (0)
