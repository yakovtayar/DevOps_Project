import requests
import pymysql
import db_connector
from selenium import webdriver


# POST REQUEST:
res = requests.post('http://127.0.0.1:5000/users/777', json={"user_name": "RONALDO"})
if res.text.__contains__("error"):
    print("POST TEST ERROR:")
    print(res.json())
    exit()
else:
    print(res.json())
# if res[0] != "ok":
#     print("error")
# print(res.text)

# GET REQUEST:
res = requests.get('http://127.0.0.1:5000/users/777')
if res.text.__contains__("error"):
    print("GET TEST ERROR:")
    print(res.json())
    exit()
else:
    print(res.json())


# Checks is the data was stored in the DB
db_connector.db_checking_for_combined_testing(777)

# Checks if the user name is correct
driver = webdriver.Chrome(executable_path="C:/Users/Yakov/Desktop/chromedriver_win32/chromedriver.exe")
driver.get("http://127.0.0.1:5001/users/get_user_data/777")
print(driver.find_element_by_id("user").text)
