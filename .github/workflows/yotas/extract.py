import urllib.request
import json

url = "https://miniyotas.osscameroon.com/v1/api/records"
response = urllib.request.urlopen( url )

data_json = json.loads( response.read() )
message = " Number of yotas each member has"

print(message)
print("```")

data_json.sort(key = lambda item: int(item['yotas']), reverse = True)
for item in data_json:
    if int(item['yotas']) > 0:
        print(item['github_handle'], "->", item['yotas'], "Yts")

print("```")
    
    
    
    
    

 

    


