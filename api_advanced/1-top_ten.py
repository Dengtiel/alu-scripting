#!/usr/bin/python3
""" A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit. """
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts in a given subreddit. """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the subreddit is valid
        if response.status_code != 200:
            print(None)
            return

        # Parse the response JSON
        data = response.json()
        
        # Ensure data structure is correct
        if 'data' not in data or 'children' not in data['data']:
            print(None)
            return

        # Extract and print post titles
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])

    except requests.exceptions.RequestException:
        print(None)
    except ValueError:  # Handles JSON decoding errors
        print(None)

