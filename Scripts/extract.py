import requests
import json

def extract_data_from_dummy_api():
    # Replace this URL with the endpoint of your dummy API
    url_0 = 'https://jsonplaceholder.typicode.com/posts'  # Example URL of a dummy API (JSONPlaceholder)

    try:
        response = requests.get(url_0)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None

def main():
    extracted_data = extract_data_from_dummy_api()
    if extracted_data:
        # For example, print the extracted data
        print("Extracted Data:")
        print(json.dumps(extracted_data[:5], indent=2))  # Print first 5 items as an example

        # You can proceed with transforming and processing this data here


        

if __name__ == "__main__":
    main()
