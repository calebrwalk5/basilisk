import requests
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import time

# Set the search term
search_term = 'test'

# Send a GET request to the Google Search page
response = requests.get('https://www.google.com/search?q=' + search_term + '+filetype:txt')

# Print the response status code to check for errors
print(response.status_code)

# Parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# Find all of the a tags that contain the .txt file extension
links = soup.find_all('a', href=lambda href: href and '.txt' in href)

# Print the number of links found to check for errors
print(len(links))

# Download the .txt files
for link in links:
    time.sleep(5) # Wait 5 seconds so we don't get 503'd
    file_url = link['href']
    # Parse the URL query parameters
    query_params = urllib.parse.parse_qs(urllib.parse.urlsplit(file_url).query)
    # Get the actual file URL from the q parameter
    actual_url = query_params['q'][0]
    # Download the file from the actual URL
    urllib.request.urlretrieve(actual_url, actual_url.split('/')[-1])

# Initialize an empty string to store the combined contents of the text files
combined_text = ''

# Iterate over the downloaded text files
for file in links:
    # Open the text file in read mode
    with open(file, 'r') as f:
        # Read the contents of the text file
        file_contents = f.read()
        # Append the contents to the combined string
        combined_text += file_contents

# Write the combined string to a new text file
with open('combined_text.txt', 'w') as f:
    f.write(combined_text)
