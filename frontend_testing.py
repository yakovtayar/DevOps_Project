from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/Yakov/Desktop/chromedriver_win32/chromedriver.exe")
driver.get("http://127.0.0.1:5001/users/get_user_data/1")
print(driver.find_element_by_id("user").text)