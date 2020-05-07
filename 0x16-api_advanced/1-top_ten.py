#!/usr/bin/python3
""" Function to get first 10 hot post """
import requests


def top_ten(subreddit):
    """ get top 10 hot post """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {
        'User-agent': 'Mozilla/5.0'
    }
    limit = {
        'limit': 10
    }
    re = requests.get(url, headers=header, allow_redirects=False, params=limit)

    if re.status_code is 200:
        re = re.json()
        top = re.get('data').get('children')
        for dic in top:
            dic = dic.get('data')
            print(dic.get('title'))
    else:
        print(None)
