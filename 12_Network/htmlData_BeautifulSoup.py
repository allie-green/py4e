from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags_sum = 0
total_tags = 0

# Retrieve all of the span tags
span_tags = soup('span')
for tag in span_tags:
    total_tags += 1
    content = int(tag.contents[0])
    tags_sum += content
    
print('Total span tags: ', total_tags)
print("Span's content sum: ", tags_sum)