import requests

# POST REQUEST:
res = requests.post('http://127.0.0.1:5000/users/10', json={"user_name": "messi"})
print(res.json())

# GET REQUEST:
res = requests.get('http://127.0.0.1:5000/users/10')
print(res.json())

# DELETE REQUEST:
res = requests.delete('http://127.0.0.1:5000/users/10')
print(res.json())





