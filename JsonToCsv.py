import csv
import json

def json_to_csv(json_file, csv_file):
    # Read JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Open CSV file for writing
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write header using keys from the JSON data
        writer.writerow(data[0].keys())
        
        # Write rows using values from the JSON data
        for row in data:
            writer.writerow(row.values())

# Example usage
json_to_csv('data.json', 'data.csv')