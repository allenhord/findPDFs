from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urljoin, urldefrag

response = requests.get(sys.argv[1])

hostPath = sys.argv[1]

soup = BeautifulSoup(response.text, 'html.parser')

for links in soup.find_all('a'):
    if "http" not in links:
        url = urljoin(hostPath, links.get('href'))
        currentResponse = (requests.head(url, allow_redirects=True))
        currentType = currentResponse.headers['Content-Type']
        if currentType == 'application/pdf':
            print("URI: {}".format(url))
            print("Final URI: {}".format(currentResponse.url))
            print("Content Length: {} bytes\n".format(currentResponse.headers['Content-Length']))

    else:
        currentResponse = (requests.head(links.get('href'), allow_redirects=True))
        print("currentResponse: {}".format(currentResponse))
        currentType = currentResponse.headers['Content-Type']
        if currentType == 'application/pdf':
            print("URI: {}".format(links.get('href')))
            print("Final URI: {}".format(currentResponse.url))
            print("Content Length: {} bytes\n".format(currentResponse.headers['Content-Length']))
