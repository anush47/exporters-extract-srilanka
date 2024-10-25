import requests
from bs4 import BeautifulSoup
import csv
import os

# Dictionary with base URLs as keys and number of pages as values
urls_and_pages = {
    "https://www.srilankabusiness.com/exporters-directory/apparel-exporters-in-sri-lanka": 14,
    # Add more URLs and their respective page numbers here
}

# Ensure the 'exporters' directory exists
os.makedirs('exporters', exist_ok=True)

# Iterate over each base URL and its number of pages
for base_url, number_of_pages in urls_and_pages.items():
    # Ensure no trailing slash in the base URL
    if base_url.endswith('/'):
        base_url = base_url[:-1]
    
    # List to store all exporter names for the current URL
    all_exporters = []
    
    # Iterate over each page
    for page in range(1, number_of_pages + 1):
        # Print progress
        print(f"Processing page {page} of {number_of_pages} for {base_url}...")
        
        # Construct the URL for the current page
        url = f"{base_url}/page{page}.html"
        
        # Send a GET request to the page
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the page content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extracting a list of exporters
            exporters = soup.find_all('h4')
            
            # Add the exporter names to the list
            for exporter in exporters:
                all_exporters.append(exporter.text.strip())
        else:
            print(f"Failed to retrieve page {page} for {base_url}")
    
    # Extract the last part of the base URL for the CSV filename
    filename = os.path.join('exporters', base_url.split('/')[-1] + '.csv')
    
    # Write all exporter names to a CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['Exporter'])
        
        # Write the exporter names
        for exporter in all_exporters:
            writer.writerow([exporter])
