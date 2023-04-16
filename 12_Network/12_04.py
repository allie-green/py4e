# 12_04
import urllib.request
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
url = 'https://www.python.org/'
html = urllib.request.urlopen(url, context=ctx).read()
paragraphs = re.findall('<p>.*?</p>'.encode(), html)

for p in paragraphs:
    count += 1
    # print(p.decode())

print(f'The are {count} paragraphs in this website.')