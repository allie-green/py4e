# NOTES
# (1) Ignore SSL certificate errors.
# (2) We are working with the following link:
#     http://py4e-data.dr-chuck.net/known_by_Brenna.html
# (3) Since we are only interested in the tag at position number 18, we will only obtain the first 18 tags.
#     The limit is set to prevent unnecessary iterations.
# (4) The index of the tag in position 18 is 17, as indexing starts at 0.
# (5) When working with a position value of 18 and a count of 7, the last name that will be printed is "Lucy".

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# (1)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ') # (2)
position = int(input('Enter position: ')) 
count = int(input('Enter count: '))
i = 0

def followingLinks(url, position):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    a_tags = soup('a', limit=position) # (3)
    anchor = a_tags[position -1] # (4)
    address = anchor.get('href', None)
    return address

while i < count:
    print('\nRetrieving:', url)
    list_owner = re.findall('by_([A-Z].+).html',url)[0]
    url = followingLinks(url, position)
    name = re.findall('by_([A-Z].+).html',url)[0]

    print(f'In the list of {list_owner}, the person in position number {position} is {name}') # (5)
    i += 1