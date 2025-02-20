#!/usr/bin/python3
"""
2. Recurse it!
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetches all hot post titles from a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): A list to store post titles.
        after (str, optional): The pagination parameter for recursion.

    Returns:
        list: A list of post titles if the subreddit is valid, otherwise None.
    """
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check for invalid subreddit
        if response.status_code != 200:
            return None

        data = response.json()
        
        # Ensure proper data structure
        if 'data' not in data or 'children' not in data['data']:
            return None

        # Extract post titles
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        # Handle pagination with recursion
        after = data['data']['after']
        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except requests.exceptions.RequestException:
        return None
    except ValueError:  # Handles JSON decoding errors
        return None

