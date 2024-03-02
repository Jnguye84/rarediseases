import requests

def get_authors_from_crossref(query):
    base_url = "https://api.crossref.org/works"
    params = {"query": query}

    # Make a request to Crossref Metadata API
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Extract author names from the API response
        works = data.get('message', {}).get('items', [])
        authors = [author for work in works for author in work.get('author', [])]

        return authors

    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")
        return None

# Example usage
disease_query = "Behcet's disease"
authors_list = get_authors_from_crossref(disease_query)

if authors_list:
    print(f"Authors related to {disease_query}:")
    for author in authors_list:
        print(author.get('given', '') + ' ' + author.get('family', ''))
