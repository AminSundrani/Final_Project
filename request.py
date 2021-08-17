import requests

url = 'http://localhost:5000/api'
r = requests.post(url,json={'values': 20000000})
print(r.json())