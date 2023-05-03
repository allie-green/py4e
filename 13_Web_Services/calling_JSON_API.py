import urllib.request, urllib.parse
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service_url = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

while True:
    print('\nEnter location, or press ENTER to exit.')
    address = input('Location: ')
    if len(address) == 0 : break

    search_parms = dict()
    search_parms["address"] = address
    search_parms["key"] = api_key

    url = service_url + urllib.parse.urlencode(search_parms)
    print('\nRetrieving:', url)

    open_url = urllib.request.urlopen(url, context=ctx)
    data = open_url.read().decode()

    try:
        json_data = json.loads(data)
    except:
        json_data = None

    if not json_data or 'status' not in json_data or json_data["status"] != 'OK':
        print('\n----- FAILURE TO RETRIEVE DATA -----')
        print(data)
        continue
    
    formatted_address = json_data["results"][0]["formatted_address"]
    place_id = json_data["results"][0]["place_id"]

    print('Formatted address:', formatted_address)
    print('Place ID:', place_id)