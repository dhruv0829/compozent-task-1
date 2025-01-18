import requests

def fetch_data_from_api():
    # Example: Fetching posts from JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Displaying the title of the first post
        print(f"Title of the first post: {data[0]['title']}")
        print(f"Title of the second post: {data[1]['title']}")
        print(f"Title of the third post: {data[2]['title']}")
        print(f"Title of the fourth post: {data[3]['title']}")
    else:
        print("Failed to fetch data from the API.")


fetch_data_from_api()
