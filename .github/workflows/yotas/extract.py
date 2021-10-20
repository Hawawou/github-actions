import urllib.request
import json

url = "https://miniyotas.osscameroon.com/v1/api/records"
response = urllib.request.urlopen( url )

data_json = json.loads( response.read() )
message = " Number of yotas each member has"

print(message)
print("```")

for item in data_json:
    print(item['github_handle':], item['yotas'])
    print("```")
    
    
    
    
    

 

    


