import urllib.request, urllib.parse
import json

service_url = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

location = input('Enter a country: ')
if len(location) < 1 : exit

parms = {}
parms["address"] = location
parms["key"] = api_key

url = service_url + urllib.parse.urlencode(parms)
open_url = urllib.request.urlopen(url)
read_url = open_url.read().decode()

data = json.loads(read_url)

try:
    country_code = data["results"][0]["address_components"][-1]["short_name"]
except:
    country_code = None

# Country codes are limited to 3 letters max.
if country_code == None or len(country_code) > 3: 
    print('Sorry, there is no country code for this location.')
else:
    print(f'The country code for this location is {country_code}')