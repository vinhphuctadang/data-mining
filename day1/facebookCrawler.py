# Usage
# <script> <facebookHandle> fromPost toPost
# E.g. facebookCrawler.py 0 10
#
# Samples are saved in fbposts.txt automatically
# what to crawl ?
# 'ownerName', 'wallOf', 'ownerUrl', "dateTime", "commentCount", "reactions", "text", "urlAttached", 
# ownerName: Name of the post owner
# wallOf: homepage of 
# ownerUrl: owner profile url 
# dateTime: date when post created 
# urlAttached: url attached to the post
# text : post text content
# reactions: raw value from facebook post from which we could see reaction
# "dateScrape": Unix timestamp when the sample is recorded

# error trace
import traceback
import time 
# load config:
import json

######### .env file ###################################
# { 
#     "FBNAME": "loginEmail@gmail.com"
#     "FBPASS": "HelloWorld"
# } 
# # It is not my actual cred, you know why !
#######################################################

with open('.env', 'r', encoding='utf8') as f:
    config = json.loads(str(f.read()))

# more sorts of config
# fault tolerance: if cannot get this post 'tolerance' times, we skip the post
tolerance = 5
outputFile = 'fbposts.txt'

# use seleneum "pip3 install selenium"
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# driver using Chrome driver, install at https://chromedriver.chromium.org
driver = webdriver.Chrome(chrome_options=chrome_options)

# schema 
# header = [
#     'wallOf', 'ownerName', 'ownerUrl', "dateTime", "text", "urlAttached"
# ]

# functions
BASEURL = 'https://facebook.com'
def __(path):
    return BASEURL+path
    
def login():
    driver.get(__('/'))

    emailInput = driver.find_element_by_xpath('//input[@name="email"]')
    passInput = driver.find_element_by_xpath('//input[@name="pass"]')
    # NOTE: Replace your username here
    emailInput.send_keys(config["FBNAME"])
    # NOTE: Replace your password here in .env File
    passInput.send_keys(config["FBPASS"])

    submit = driver.find_element_by_xpath('//button[@name="login"]')
    submit.click()
    time.sleep(3)

def extractPostInfo(focusHandle, post):

    # people who relate to the post
    peopleTags = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span/h2')
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
    contentPanes = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[3]')
    postText = '\n'.join([pane.text for pane in contentPanes])
    
    # url attached to the url
    urls = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/div/a')
    urlAttached = ""
    if len(urls):
        urlAttached = urls[0].get_attribute("href")
    else:
        print('No url attached for post of ' + ownerName)

    # find number of comments
    commentTag = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/span')
    commentCount = 0
    if len(commentTag):
        commentCountStr = commentTag[0].text
        commentCount    = int(commentCountStr[:commentCountStr.find(' ')])
    
    # find reaction string:
    reactionTag = post.find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[2]/span/span')
    reactionText = ""
    if len(reactionTag):
        reactionText = reactionTag[0].text 

    # return value
    return {
        "wallOf": focusHandle, 
        "ownerName": ownerName,
        "ownerUrl": ownerUrl,
        "dateTime": dateTime,
        "text": postText,
        "urlAttached": urlAttached,
        "commentCount": commentCount,
        "reactions": reactionText,
        "dateScrape": int(time.time())
    }

def goToWallOf(handle):
    driver.get(__('/'+handle))
    time.sleep(2)

def main():

    import sys 
    focusHandle = sys.argv[1]
    # start post index, from 0

    # says, the post divison starts from index 3
    START = int(sys.argv[2])+3

    # end post index (START..<DEST)
    DEST = int(sys.argv[3])+3

    # login with given cred
    login()

    goToWallOf(focusHandle)

    # open file for writing data
    f = open(outputFile, 'a')
    
    i = START
    fault_count = 0
    try: 
        while i < DEST:
            # find post tag
            post = driver.find_elements_by_xpath(
                f'//html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[{i}]'
            )
            
            if fault_count >= tolerance:
                print('Tolerance exceeds, move to next post')
                i += 1
                continue

            if not len(post): # No Such element
                # then load more, scroll down
                print('Post not found, scrolling down to see more')
                driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
                fault_count += 1
                time.sleep(5)
                continue

            owner = post[0].find_elements_by_xpath('.//div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span/h2')
            if not len(owner):
                # in case post could not load, we may want to load more by scrolling down 
                print('No owner found, post empty, we want to scroll')
                driver.execute_script("window.scrollBy(0, document.body.scrollHeight)") 
                fault_count += 1
                time.sleep(5)
                continue

            print('----------------------------')
            # reset fault
            fault_count = 0 
            post = post[0]
            try: 
                postInfo = extractPostInfo(focusHandle, post)
                print(postInfo)

                # write result to file
                f.write('%s\n'% json.dumps(postInfo, ensure_ascii=False))
            except Exception as e:
                traceback.print_tb(e.__traceback__)
            i+=1
    # in case we want to break
    except KeyboardInterrupt:
        f.close()
        return 
    f.close()
main()