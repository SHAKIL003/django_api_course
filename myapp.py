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

## Inserting Data
# URL = "http://127.0.0.1:8000/studentcreate/"
# data = {
#     'name':'Haroon',
#     'roll':106,
#     'city':'Islamabad'
# }
# json_data = json.dumps(data)
# r = requests.post(url=URL, data=json_data)
# data = r.json()
# print(data)

## CRUD
URL = "http://127.0.0.1:8000/drfapi/"
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# get_data()

def post_data():
    data = {
    'name':'Major Ikram',
    'roll':104,
    'city':'Bangladesh'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers,data=json_data)
    data = r.json()
    print(data)
# post_data()

def update_data():
    data = {
    'id': 4,
    'name': 'Major Sayyed Ikram Ullah Khan',
    'roll' : 104,
    'city':'Lahore'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers,data=json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = {'id': 4}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,headers=headers,  data=json_data)
    data = r.json()
    print(data)

delete_data()