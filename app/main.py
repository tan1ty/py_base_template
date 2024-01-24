import requests


def fetch_data(url):
    """Fetch data from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()  # Returns the response in JSON format
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def main():
    """Main function to execute the script actions."""
    print("Fetching data from JSONPlaceholder API...")
    data = fetch_data("https://jsonplaceholder.typicode.com/todos/1")
    if data:
        print(f"Data fetched successfully: {data}")


if __name__ == "__main__":
    main()

