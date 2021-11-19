import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'latitude':2, 'longitude':9})

print(r.json())