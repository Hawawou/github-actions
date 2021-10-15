import urllib.request
import json
# import pandas

url = "https://miniyotas.osscameroon.com/v1/api/records"
response = urllib.request.urlopen( url )

data_json = json.loads( response.read() )

for item in data_json:
    print (item['github_handle'], item['yotas'])

 

    
    

