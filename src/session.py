import time
from selenium import webdriver

class Session:

    def __init__(self, _file: str):
        self.code = None
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

    def get_credentials(self):
        '''
        get client_secret and client_id
        '''

        wd = webdriver.Safari()
        wd.get('https://www.strava.com/settings/api')

        cookies_button = wd.find_element_by_xpath('//*[@id="stravaCookieBanner"]/div/div/button')
        cookies_button.click()

        wd.find_element_by_id('email').send_keys(self.mail)
        wd.find_element_by_id('password').send_keys(self.pswd)

        login_button = wd.find_element_by_id('login-button')
        login_button.click()

        time.sleep(2)

        # secret_button = wd.find_element_by_id('show-secret')
        # secret_button.click()

        token_button = wd.find_element_by_id('show-token')
        token_button.click()

        _access_token = wd.find_element_by_xpath('//*[@id="API"]/table/tbody/tr[5]/td[2]/span')
        # _renew = wd.find_element_by_xpath('//*[@id="API"]/table/tbody/tr[6]/td[2]/span')

        self.client_id = wd.find_element_by_xpath('//*[@id="API"]/table/tbody/tr[3]/td[2]').get_attribute('innerHTML')
        self.access_token = _access_token.get_attribute('innerHTML')
        # renew = _renew.get_attribute('innerHTML')

        # self.balise = renew

        wd.quit()
        return None

