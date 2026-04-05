#!/usr/bin/python3
"""
This module contains a script that consumes data from a REST API
and prints the status code and title of the first post.
"""
import requests


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints specific details.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # 1. Perform the GET request
    response = requests.get(url)
    
    # 2. Print the status code (e.g., 200 for success)
    print("Status Code: {}".format(response.status_code))
    
    # 3. If successful, parse the JSON and print the first title
    if response.status_code == 200:
        posts = response.json()
        if posts:
            print("First Post Title: {}".format(posts[0].get('title')))


if __name__ == "__main__":
    fetch_and_print_posts()
