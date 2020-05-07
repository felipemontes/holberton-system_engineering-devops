#!/usr/bin/python3
""" request all the titles of a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recursive function to get all titles """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': '1.0'
    }
    params = {
        'after': after
    }
    response = requests.get(url, allow_redirects=False, headers=headers,
                            params=params)

    if response.status_code == 200:
        r = response.json()
        x = r.get('data').get('children')
        aft_val = r.get('data').get('after')
        for i in x:
            hot_list.append(i.get('data').get('title'))
        if not aft_val:
            return (hot_list)
        return (recurse(subreddit, hot_list, aft_val))
    else:
        return(None)
