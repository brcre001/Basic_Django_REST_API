import requests

endpoint = "http://localhost:8000/api/products/"
headers = { 'Authorization': 'Bearer 2fe547ac1d317c2c50012fee51e8c35099f81982'}
data = {
    "title": "This field is done",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers)
# print('Response: ', get_response)
print(get_response.json())