
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")


username = driver.find_element(By.XPATH,"//input[@id = 'user-name']")
password = driver.find_element(By.XPATH,"//input[@id = 'password']")
login = driver.find_element(By.XPATH,"//input[@type = 'submit']")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login.click()

time.sleep(1.5)

if "inventory" in driver.current_url:
    print("Login successful")
else:
    print("Login failed")

item1_add_to_cart = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")
item1_add_to_cart.click()

cart = driver.find_element(By.XPATH,"//a[@class = 'shopping_cart_link']")
cart.click()

checkout = driver.find_element(By.XPATH,"//button[@id = 'checkout']")
checkout.click()

first_name = driver.find_element(By.ID,"first-name")
last_name = driver.find_element(By.ID,"last-name")
pincode = driver.find_element(By.ID,"postal-code")

first_name.send_keys("Yash")
last_name.send_keys("Ind")
pincode.send_keys("ABCD")

ctn_btn = driver.find_element(By.ID,"continue")
ctn_btn.click()

finish = driver.find_element(By.ID,"finish")
finish.click()

if "complete" in driver.current_url:
    print("Order placed successfully")
else:
    print("Order failed")

time.sleep(1.5)