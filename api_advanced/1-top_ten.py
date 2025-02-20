#!/usr/bin/python3
"""
1. Top Ten
Fetch and print the titles of the first 10 hot posts of a given subreddit.
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

