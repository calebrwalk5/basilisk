import requests
from bs4 import BeautifulSoup
import urllib
import urllib.parse

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
    file_url = link['href']
    # Parse the URL query parameters
    query_params = urllib.parse.parse_qs(urllib.parse.urlsplit(file_url).query)
    # Get the actual file URL from the q parameter
    actual_url = query_params['q'][0]
    # Download the file from the actual URL
    urllib.request.urlretrieve(actual_url, actual_url.split('/')[-1])
