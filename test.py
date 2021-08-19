import requests

url = 'http://localhost:5000/api'
r = requests.post(url,json={'values'})
print(r.json())