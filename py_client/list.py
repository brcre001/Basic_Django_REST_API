import requests

endpoint = "http://localhost:8000/api/products/"

get_response = requests.get(endpoint)
# print('Response: ', get_response)
print(get_response.json())