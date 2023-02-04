#Starts up our Driver and loads up our starting webpage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Web Scraping course/chromedriver.exe')

driver.get('https://www.google.com/')

#inputting text into a box
box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
box.send_keys('web scraping')
box.send_keys(Keys.ENTER)


#clicking on a button
button = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
button.click()
link = driver.find_element_by_xpath('//*[@id="rso"]/div[3]/div/div[1]/a/h3').click()
data_scraping = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]/a[1]').click()


#taking a screenshot
driver.save_screenshot('C:\Web Scraping course\screenshot.png')
driver.find_element_by_xpath('//*[@id="rso"]/div[3]/div/div[1]/a/h3').screenshot('C:\Web Scraping course\screenshot2.png')

#full example - uses inputting text into a box, clicking on a button, and taking a screenshot
driver = webdriver.Chrome('C:/Web Scraping course/chromedriver.exe')
driver.get('https://www.google.com/')
box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
box.send_keys('giraffe')
box.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()
driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[3]/a[1]/div[1]/img').screenshot('C:\Web Scraping course\giraffe.png')

#self scrolling
driver.execute_script('return document.body.scrollHeight')
driver.execute_script('window.scrollTo(0,6000)')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

#wait times
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC
import time

box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
box.send_keys('giraffe')
box.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()

# So what this is going to do is it's telling the driver, which is the page here, basically, that's our driver, remember? It's telling you to wait 10 seconds.
# OK, we can put a number here, we can say to wait five seconds, wait 10 seconds to load up the next page. Until. This is it till we find a specific element.
# All right. So, for example. Washington, open up the HTML here. Now, let's say we want to wait until he finds this ID tag, whoever this is, until it finds.
# A class, if I can find a class in this class, right, until it finds something that matches something on this Web page. Until it finds a specific element of the Web page, basically.
# And there's a lot of things that we can tell it to wait until the check, for example, again, was put by Pat Dodgier, it's can load up all these so we can wait until the Web page matches a specific
# class name I.D., latex tag, name XPath.

# But we're telling our driver here, hey, wait 10 seconds until on the next page we can find this specific I.D. somewhere in the TMO.  Wait until we find it, and then when we do find it, then you can run the rest of your Web scraping
# code, but if you can't find it after 10 seconds, it's going to break. It's going to stop everything.

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'cntratet')))























