
# Replace 'path/to/chromedriver' with the actual path to your chromedriver executable
url = 'https://clinicaltrials.gov/search?cond=ADCY5&aggFilters=results:with'

# Set up the Chrome WebDriver


def get_ncts(drugname):
    import sys
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from selenium.webdriver.common.by import By

    options = webdriver.ChromeOptions()
    options.headless = True  # Set to True if you don't want a visible browser window
    driver = webdriver.Chrome(options=options)
    nct_list = []
    try:
        # Open the webpagea
        driver.get(f'https://clinicaltrials.gov/search?cond={drugname}')

        # Wait for the page to load (you may need to adjust the wait time)
        driver.implicitly_wait(10)

        # Find all div elements with class "nct-id"
        nct_id_elements = driver.find_elements(By.CLASS_NAME, 'nct-id')

        # Extract and print the content of each div
        for element in nct_id_elements:
            nct_id = element.text
            nct_list.append(nct_id)

    finally:
        # Close the browser window
        driver.quit()
    return nct_list
        
# print(get_ncts("ADCY5"))

# def main():
#     drugname = sys.argv[1]

#     list = get_ncts(drugname)
#     print(list)
#     return(list)

# if __name__ == "__main__":
#     main()
# #call using python3 /Users/manas/Documents/GitHub/trading/virtenv/get_ncts.py Exparel
    
# sys.exit()