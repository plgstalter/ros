import time
from selenium import webdriver

class Session:

    def __init__(self, client_id):
        self.code = None
        self.client_id= client_id

    def __repr__(self) -> str:
        return f'instance du client {self.client_id}'

    def grant_access(self):
        wd = webdriver.Safari()

        wd.get(f'http://www.strava.com/oauth/authorize?client_id={self.client_id}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all')
        # time.sleep(2)

        cookies_button = wd.find_element_by_xpath('//*[@id="stravaCookieBanner"]/div/div/button')
        cookies_button.click()

        file = open('logins.txt')

        wd.find_element_by_id('email').send_keys(file.readline()[:-1])
        wd.find_element_by_id('password').send_keys(file.readline()[:-1])

        login_button = wd.find_element_by_id('login-button')
        login_button.click()

        file.close()

        time.sleep(2)

        aut_button = wd.find_element_by_id('authorize')
        aut_button.click()

        time.sleep(2)
        url = wd.current_url

        wd.quit()

        self.code = url
        return None
