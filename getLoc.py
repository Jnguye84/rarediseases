import requests

def get_last_affiliation(researcher_name):
    base_url = "https://api.crossref.org/works"
    params = {"query.author": researcher_name}

    # Make a request to Crossref Metadata API
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Extract relevant information from the API response
        works = data.get('message', {}).get('items', [])

        for work in works:
            # Get the first author's affiliation
            author_affiliation = work.get('author', [{}])[0].get('affiliation', 'N/A')

            # Check if affiliation information is available
            if author_affiliation:
                # Assuming the last affiliation in the list is the most recent
                last_affiliation = author_affiliation[-1].get('name', 'N/A')
                return last_affiliation

        print(f"No affiliation information found for {researcher_name}")
        return None

    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")
        return None

# Example usage
researcher_name = "Hulya Nazik"
last_affiliation = get_last_affiliation(researcher_name)

if last_affiliation:
    print(f"{researcher_name}'s last affiliation: {last_affiliation}")