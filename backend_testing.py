import requests
import pymysql
import db_connector

# POST REQUEST:
try:
    res = requests.post('http://127.0.0.1:5000/users/777', json={"user_name": "RONALDO"})
except:
    print(res.json())
# GET REQUEST:
try:
    res = requests.get('http://127.0.0.1:5000/users/777')
except:
    print(res.json())


print(db_connector.db_checking_for_backend_testing(777))