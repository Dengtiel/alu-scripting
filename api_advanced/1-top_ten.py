#!/usr/bin/python3
"""
Reddit API - Top Ten Hot Posts

This module contains a function that queries the Reddit API to fetch and print
the titles of the first 10 hot posts from a given subreddit.

Functions:
    - top_ten(subreddit): Fetches and prints the first 10 hot post titles.
    
Usage:
    The function should be called with the subreddit name as an argument.
    If the subreddit is invalid or inaccessible, it prints "None".

Example:
    >>> top_ten("python")
    Python 3.11 is out now!
    Best resources to learn Python?
    How do I improve my Python skills?
    ...
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None: Prints the titles if valid, otherwise prints "None".
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Handle invalid subreddit
        if response.status_code != 200:
            print("None")
            return

        data = response.json()

        # Ensure the response contains valid post data
        if 'data' not in data or 'children' not in data['data']:
            print("None")
            return

        # Extract and print the first 10 post titles
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])

    except requests.exceptions.RequestException:
        print("None")
    except ValueError:  # Handles JSON decoding errors
        print("None")
