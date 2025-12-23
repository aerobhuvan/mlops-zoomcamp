import requests

ride = {
    "PULocationID": 20,
    "DOLocationID": 100,
    "trip_distance": 4000
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=ride)
print(response.json())
