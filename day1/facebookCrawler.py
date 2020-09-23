# what to crawl ?
# id, customName, email, phone number, friend Number
import time 
# load config:
import json
# {
#     "FBPASS": "HelloWorld"
# } # It is not my actual password, you know why 

with open('.env', 'r', encoding='utf8') as f:
    config = json.loads(str(f.read()))

# use seleneum
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# new driver
driver = webdriver.Chrome(chrome_options=chrome_options)

# functions
BASEURL = 'https://facebook.com'
def __(path):
    return BASEURL+path
def login():
    driver.get(__('/'))

    emailInput = driver.find_element_by_xpath('//input[@name="email"]')
    passInput = driver.find_element_by_xpath('//input[@name="pass"]')
    # NOTE: Replace your username here
    emailInput.send_keys("vinhphuctadang@gmail.com")
    # NOTE: Replace your password here in .env File
    passInput.send_keys(config["FBPASS"])

    submit = driver.find_element_by_xpath('//button[@name="login"]')
    submit.click()
    time.sleep(3)
    
def goToWallOf(handle):
    driver.get(__('/'+handle))
    
    introduce = driver.find_element_by_xpath('//div[@role="main"]')
    # introduce.
    print(introduce.text)


login()
goToWallOf('vinhphuc.tadang')
