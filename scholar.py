from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def get_author_and_citations_selenium(query):
    base_url = "https://scholar.google.com/scholar"
    
    # Initialize the Chrome driver (you can use other drivers too)
    driver = webdriver.Chrome()

    try:
        # Open Google Scholar
        driver.get(base_url)

        # Find the search input field and enter the query
        search_input = driver.find_element("name", "q")
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

        # Wait for the results page to load
        driver.implicitly_wait(5)  # Adjust the wait time as needed

        # Get the HTML of the page
        page_html = driver.page_source

        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(page_html, 'html.parser')

        # Extract information for each search result
        search_results = soup.select('.gs_ri')  # Assumes each search result is inside an element with class 'gs_ri'

        # Initialize a list to store nested lists for each result
        results_list = []

        for result in search_results:
            # Extract author names
            author_elements = result.select_one('.gs_a')
            authors = author_elements.get_text() if author_elements else "N/A"

            # Extract citations
            citations_element = result.select_one('.gs_fl a')
            citations = citations_element.get_text() if citations_element else "N/A"

            # Append a nested list [authors, citations] to the results list
            results_list.append([authors, citations])

        return results_list

    finally:
        # Close the browser window
        driver.quit()

# Example usage
disease_query = "Behcet's disease"
results_list = get_author_and_citations_selenium(disease_query)

if results_list:
    print(f"Results for {disease_query}:")
    for result in results_list:
        print(f"Authors: {result[0]}, Citations: {result[1]}")
