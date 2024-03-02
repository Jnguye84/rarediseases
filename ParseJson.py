import csv
import json

# Read JSON data from file
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)

# Extracting data
data_to_write = []
for item in json_data:
    entry = item.get('entry')
    if entry:
        allelic_variant_list = entry.get('titles', {}).get('preferredTitle', '')
        reference_list = entry.get('referenceList', [])
        # contributors = entry.get('contributors', '')  # Contributors not provided in the JSON

        contributors = entry.get('contributors', '')  # Extract contributors from the JSON
        contributors_names = [contributor.split('-')[0].strip() for contributor in contributors.split('\n')]  # Extract names only

        for reference in reference_list:
            reference_data = reference.get('reference', {})
            if reference_data:
                external_link = "https://doi.org/" + reference_data.get('doi', '')  # Construct external link
                for contributor_name in contributors_names:
                    data_to_write.append([allelic_variant_list,
                                          reference_data.get('source', ''),
                                          external_link,
                                          contributor_name])

# Writing to CSV
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Allelic variant list', 'Reference list', 'External links', 'Contributors'])
    writer.writerows(data_to_write)

print("CSV file 'output.csv' created successfully!")
