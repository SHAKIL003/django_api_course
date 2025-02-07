# import requests
# URL = "http://127.0.0.1:8000/studentdetail/1"

# r = requests.get(url = URL)

# data = r.json()
# print(data)

import requests
import json
# URL = "http://127.0.0.1:8000/studentinfo/4"

# r = requests.get(url=URL)

# print(r.text)  # Print the raw response content

# try:
#     data = r.json()
#     print(data)
# except ValueError:
#     print("The response is not a valid JSON")

URL = "http://127.0.0.1:8000/studentcreate/"
data = {
    'name':'Haroon',
    'roll':106,
    'city':'Islamabad'
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
