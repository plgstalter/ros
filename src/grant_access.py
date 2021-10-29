import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium .webdriver.common.keys import Keys

# Safari webdriver used in selenium

wd = webdriver.Safari()


wd.get(f'http://www.strava.com/oauth/authorize?client_id={argv[1]}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all')

cookies_button = wd.find_element_by_xpath('//*[@id="stravaCookieBanner"]/div/div/button')
cookies_button.click()
time.sleep(1)

file = open('logins.txt')

wd.find_element_by_id('email').send_keys(file.readline()[:-1])
wd.find_element_by_id('password').send_keys(file.readline()[:-1])

login_button = wd.find_element_by_id('login-button')
login_button.click()

file.close()

time.sleep(1)

aut_button = wd.find_element_by_id('authorize')
aut_button.click()

time.sleep(2)

url = wd.current_url

print(url)

wd.quit()
