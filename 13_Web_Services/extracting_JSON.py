from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1732420.json'
open_url = urlopen(url, context=ctx)
content = open_url.read().decode()
content_json = json.loads(content)

total_sum = 0
for c in content_json["comments"]:
    total_sum += int(c["count"])

characters = len(content)
users = len(content_json["comments"])

print(f'\nRetrieving: {url}')
print(f'Characters retrieved: {characters}')
print(f'Number of users who commented: {users}')
print(f'Total sum of comments: {total_sum}\n')