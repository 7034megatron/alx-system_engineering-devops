#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Construct the URL for the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
    except KeyError:
        # Handle cases where the subreddit is invalid or does not exist
        print(f"Subreddit '{subreddit}' not found.")
        return 0

if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    print("Number of subscribers:", number_of_subscribers(subreddit))
