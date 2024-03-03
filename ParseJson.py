import csv
import json

# Read JSON data from file
with open('data.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

from get_ncts import get_ncts
from getLoc import get_last_affiliation
import csv

def main(ncts):
    # import subprocess
    # subprocess.run(["pip", "install", "selenium"])
    import sys
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    class ClinicalTrialsInfo:
        def __init__(self, NCTid):
            self.url = "https://clinicaltrials.gov/study/" + str(NCTid).strip(',') # + "?aggFilters=results:with&rank=1&tab=results"
            self.adverse_events = None
            self.collaborators = None

        def get_adverse_events(self):
            driver = webdriver.Chrome()  # You can change this according to your WebDriver

            try:
                driver.get(self.url)
                element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "adverse-events"))
                )

                element_list = element.text.split("\n")
                element_list = element_list[element_list.index('Serious Adverse Events'):]
                totals = []
                totals_indices = []
                for index, item in enumerate(element_list):
                    if "Total" in item.split(" "):
                        totals.append(item)
                        totals_indices.append(index)
                for index, item in enumerate(element_list):
                    if index > max(totals_indices) and "%" in list(item):
                        totals.append(item)

                self.adverse_events = totals

            finally:
                driver.quit()

        def get_collaborators(self):
            driver = webdriver.Chrome()  # You can change this according to your WebDriver

            try:
                driver.get(self.url)
                element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "contacts-box"))
                )

                # Extract text within the "contacts-box" div
                contacts_text = element.text
                # print(contacts_text)
                # Split the text based on newline character to get a list of lines
                contacts_lines = contacts_text.split("\n")

                # Extract collaborators by excluding the labels (e.g., "Sponsor", "Collaborators", "Investigators")
                colabs = [line.strip() for line in contacts_lines if line.lower() not in ["sponsor", "collaborators", "investigators"]]

                self.collaborators = colabs

            finally:
                driver.quit()

    def get_adverse_events(nct_list):
        adverse_events = []

        for nct in nct_list:
            try:
                trial_info = ClinicalTrialsInfo(nct)
                
                trial_info.get_adverse_events()

                adverse_events.append(trial_info.adverse_events)
            except Exception as e:
                
                # print(f"Error processing NCT ID {nct}: {str(e)}")
                adverse_events.append(None)  

        return adverse_events


    def get_collabs(nct_list):
        collabs = []

        for nct in nct_list:
            try:
                trial_info = ClinicalTrialsInfo(nct)
                
                trial_info.get_collaborators()

                collabs.append(trial_info.collaborators)
            except Exception as e:
                
                print(f"Error processing NCT ID {nct}: {str(e)}")
                collabs.append(None)  

        return collabs
    return get_collabs(ncts)
# print(main(['NCT04469283', 'NCT05136495', 'NCT04351360', 'NCT03481491']))
# print(main(get_ncts("ADCY5")))
data_str = main(get_ncts("ADCY5"))
# print(data_str)
names = []
phones_email = [] 
locations = []
for i in data_str:
    for count, j in enumerate(i):
        if 'Name' in j: 
            names.append(j[6:])
        if 'Phone Number' in j:
            phones_email.append(i[count + 1])
        if 'Email' in j:
            phones_email.append(j[7:])

for k in names:
    locations.append(get_last_affiliation(k))

# Extracting data
data_to_write = []
for item in json_data:
    entry = item.get('entry')
    if entry:
        allelic_variant_list = entry.get('titles', {}).get('preferredTitle', '')
        reference_list = entry.get('referenceList', [])
        contributors = entry.get('contributors', '')  # Extract contributors from the JSON
        contributors_names = [contributor.split('-')[0].strip() for contributor in contributors.split('\n')]  # Extract names only

        for reference in reference_list:
            reference_data = reference.get('reference', {})
            if reference_data:
                external_link = "https://doi.org/" + reference_data.get('doi', '')  # Construct external link
                for contributor_name in contributors_names:
                    # Append each data point to the row
                    data_row = [allelic_variant_list,
                                reference_data.get('source', ''),
                                external_link,
                                contributor_name]

                    # Add corresponding entry from additional lists
                    if len(data_to_write) < len(names):
                        data_row += [names[len(data_to_write)], phones_email[len(data_to_write)], locations[len(data_to_write)]]

                    data_to_write.append(data_row)

# Writing to CSV
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Allelic variant list', 'Reference list', 'External links', 'Contributors', 'Name', 'Phone & Email', 'Location'])
    writer.writerows(data_to_write)

print("CSV file 'output.csv' created successfully!")