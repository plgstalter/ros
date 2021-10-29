import time
from selenium import webdriver

class Session:

    def __init__(self, client_id: int, _file: str):
        self.code = None
        self.client_id = client_id
        file = open(_file, 'r')
        self.mail = file.readline()[:-1]
        self.pswd = file.readline()[:-1]

    def __repr__(self) -> str:
        return f'instance du client {self.client_id}'

    def grant_access(self):
        '''
        aims to grant access to the strava api
        '''

        wd = webdriver.Safari()
        wd.get(f'http://www.strava.com/oauth/authorize?client_id={self.client_id}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all')

        cookies_button = wd.find_element_by_xpath('//*[@id="stravaCookieBanner"]/div/div/button')
        cookies_button.click()

        wd.find_element_by_id('email').send_keys(self.mail)
        wd.find_element_by_id('password').send_keys(self.pswd)

        login_button = wd.find_element_by_id('login-button')
        login_button.click()

        time.sleep(2)

        aut_button = wd.find_element_by_id('authorize')
        aut_button.click()

        time.sleep(2)

        url = wd.current_url
        wd.quit()

        #isolating the part of the url containing the code
        start = url.find('code')
        end = url.find('&scope')

        self.code = url[(start+ 5):end]
        return None

