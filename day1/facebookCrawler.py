# what to crawl ?
# id, personId, post_date, postTitle
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

# schema 
header = [
    'ownerName', 'ownerUrl', "dateTime", "text", "urlAttached"
]

# functions
BASEURL = 'https://facebook.com'
def __(path):
    return BASEURL+path

# def tryFindElementByXPath(xpath):
#     from selenium.common.exceptions import NoSuchElementException
#     try:
#         return driver.find_element_by_xpath(xpath)
#     except NoSuchElementException:
#         return None
    
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

def extractPostInfo(focusHandle, post):
    print(post.text)
    # import re
    # people who relate to the post
    peopleTags = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span/h2')
    # /html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[6]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span/h2/strong[1]/span/a/div/span
    # urls of peoples
    ownerUrls = peopleTags[0].find_elements_by_xpath('.//a')
    # we only consider owner
    ownerName = ownerUrls[0].text
    
    # also get url
    ownerUrl = ownerUrls[0].get_attribute('href')
    ownerUrl = ownerUrl[:ownerUrl.find('?')]
    
    # date time:
    dateTimeTag = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/span')
    dateTime = dateTimeTag[0].text
    dateTime = dateTime[:dateTime.find('\n')]

    # find post content
    contentPanes = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[3]/div[1]/div/div/div/span/div/div')
    postText = '\n'.join([pane.text for pane in contentPanes])
    
    urls = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/div/a')
    urlAttached = ""
    if len(urls):
        urlAttached = urls[0].get_attribute("href")
    else:
        print('No url attached for post of ' + ownerName)

    commentTag = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/span')
    commentCount = 0
    if len(commentTag):
        commentCountStr = commentTag[0].text
        commentCount    = int(commentCountStr[:commentCountStr.find(' ')])
    
    reactionTag = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[2]/span/span')
    reactionText = ""
    if len(reactionTag):
        reactionText = reactionTag[0].text 

    return {
        "wallOf": focusHandle, 
        "ownerName": ownerName,
        "ownerUrl": ownerUrl,
        "dateTime": dateTime,
        "text": postText,
        "urlAttached": urlAttached,
        "commentCount": commentCount,
        "reaction": reactionText,
        "dateScrape": int(time.time())
    }

def goToWallOf(handle):
    driver.get(__('/'+handle))
    time.sleep(2)

def main():
    login()
    focusHandle = 'vinhphuc.tadang'
    goToWallOf(focusHandle)

    f = open('fbposts.txt', 'a')
    i = 3
    DEST = 10
    try: 
        while i < DEST:

            # find post tag
            post = driver.find_elements_by_xpath(
                f'//html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{i}]'
            )
            
            if not len(post): # No Such element
                print('Post not found, scrolling down to see more')
                driver.execute_script("window.scrollBy(0, document.body.scrollHeight)") 
                time.sleep(5)
                continue

            owner = post[0].find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span/h2')
            if not len(owner):
                print('No owner found, post empty, we want to scroll')
                driver.execute_script("window.scrollBy(0, document.body.scrollHeight)") 
                time.sleep(5)
                continue

            print('----------------------------')
            post = post[0]
            # try:
            postInfo = extractPostInfo(focusHandle, post)
            print(postInfo)
            f.write('%s\n'% json.dumps(postInfo, ensure_ascii=False))
            # except Exception as e:
            #     print('Extract info error:', e)

            # increase i
            i+=1
    except KeyboardInterrupt:
        f.close()

main()