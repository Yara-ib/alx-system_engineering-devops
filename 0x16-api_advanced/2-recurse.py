#!/usr/bin/python3
""" Module for queries the Reddit API, parses the title of all hot articles """
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ Function that queries the Reddit API, parses title of hot articles """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.history or response.status_code == 404:
        return None
    response = response.json()
    after = response.get('data').get('after')
    if after:
        response = response.get('data').get('children')
        for title in response:
            title = title.get('data').get('title')
            hot_list.append(title)
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
