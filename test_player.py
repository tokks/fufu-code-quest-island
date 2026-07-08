import requests

response = requests.get('http://localhost:5000/api/player')
print(f"Status: {response.status_code}")
data = response.json()
print(f"Name: {data.get('name')}")
print(f"Level: {data.get('level')}")
print(f"Is Admin: {data.get('is_admin')}")