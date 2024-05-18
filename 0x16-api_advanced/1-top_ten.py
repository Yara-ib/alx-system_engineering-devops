#!/usr/bin/python3
""" Titles of the first 10 hot posts listed for a given subreddit Module """
import requests


def top_ten(subreddit):
    """
    Getting the titles of first 10 hot posts
    listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.history or response.status_code == 404:
        print('None')
    else:
        response = response.json()
        response = response.get('data').get('children')
        for title in response:
            print(title.get('data').get('title'))
