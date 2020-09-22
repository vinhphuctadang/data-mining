# what to crawl ?
# id, customName, email, phone number, friend Number
# config:
import json
with open('.env', 'r', encoding='utf8') as f:
    config = json.loads(str(f.read()))

# use seleneum
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://facebook.com')

emailInput = driver.find_element_by_xpath('//input[@name="email"]')
passInput = driver.find_element_by_xpath('//input[@name="pass"]')
emailInput.send_keys("vinhphuctadang@gmail.com")
passInput.send_keys(config["FBPASS"])

submit = driver.find_element_by_xpath('//button[@name="login"]')
submit.click()