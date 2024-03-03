import requests
import os
import json

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'WqmAXMx3Qya11wfDRC1k0w'

# Example API endpoint URL
url = 'https://api.omim.org/api/entry/search?search=ADCY5&include=referenceList&include=externalLinks&include=contributors&format=json&start=0&limit=10&apiKey=WqmAXMx3Qya11wfDRC1k0w'

# Set up the request headers with the API key
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Make a GET request to the API endpoint with the headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Now 'data' contains the JSON response from the API
    # print(data)
    # only get the entry list
    entry_list = data['omim']['searchResponse']['entryList']
    
    # Write JSON data to a file in the same directory
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(file_path, 'w') as f:
        json.dump(entry_list, f, indent=4)
        
    print("JSON file created successfully.")
else:
    # If the request was unsuccessful, print the error message
    print(f"Error: {response.status_code} - {response.text}")