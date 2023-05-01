from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input('Enter location: ')
content = urlopen(location, context=ctx).read().decode()
tree = ET.fromstring(content)

comment_tags = tree.findall('comments/comment')
total_sum = 0

for comment in comment_tags:
    value = int(comment.find('count').text)
    total_sum += value

print('\nRetrieving:', location)
print('Count:', len(comment_tags))
print('Sum:', total_sum)
