import requests, json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb") # can replace 'se120nb' with other postcodes
# alternative url: https://pokeapi.co/api/v2/pokemon/ditto

print(post_codes_req) # <Response [200]> means successful request
print(post_codes_req.status_code) # 200
print(post_codes_req.headers) # returns headers
print(post_codes_req.content) # returns json content with b wrapping
print(post_codes_req.json()) # returns a python dict of contents

# post request to postcode.io

json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())
#print(json.dumps(post_multi_req.json(), indent=2)) # prints prettier