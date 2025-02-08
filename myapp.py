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
URL = "http://127.0.0.1:8000/studentapi/"
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data(2)

def post_data():
    data = {
    'name':'Ayaz Khan',
    'roll':107,
    'city':'Lahore'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
# post_data()

def update_data():
    data = {
    'id': 2,
    'name':'Ayaz Khan Developer',
    'city':'Swat Mingora'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = {'id': 9}

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

delete_data()