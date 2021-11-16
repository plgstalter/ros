from selenium import webdriver
import time

import selenium
#from os import system #useless for now
from session import Session
import gpxpy 

class Gpx(Session):

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"je suis un fichier gpx ! associé à l'utilisateur {self.client_id}"

    def get_gpx(self, url: str):

        # login step

        wd = webdriver.Safari()
        wd.get(f'http://www.strava.com/oauth/authorize?client_id={self.client_id}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all')

        cookies_button = wd.find_element_by_xpath('//*[@id="stravaCookieBanner"]/div/div/button')
        cookies_button.click()

        wd.find_element_by_id('email').send_keys(self.mail)
        wd.find_element_by_id('password').send_keys(self.pswd)

        login_button = wd.find_element_by_id('login-button')
        login_button.click()

        time.sleep(2)

        # time to get the activity gpx

        '''
        ...
        '''

        self.data_points = []

        gpx_file = open('file.gpx', 'r')

        _gpx_file = gpxpy.parse(gpx_file)

        for track in _gpx_file.tracks:
            for segment in track.segments:
                 for point in segment.points:
                    self.data_points.append([point.longitude, point.latitude])

        

    def add_data_points(self):

        file = open('positions.csv', 'w')

        file.close()
        return None

    def get_all_pages(self, wd: webdriver) -> None:
        compteur = 0
        current_page = 'hihi'
        _max = 10
        while compteur < _max:
            self.get_full_page(wd, current_page)


    def get_full_page(self, wd: webdriver, current_page: str) -> None:
        wd.get(current_page)
        for i in range(1, 21):
            _link = wd.find_element_by_xpath(f'//*[@id="search-results"]/tbody/tr[{i}]/td[3]/a')
            _link.click()
            time.sleep(1) # wait for load
            dl_button = wd.find_element_by_xpath('/html/body/div[2]/div[3]/nav/div/div/ul/li[8]/a')
            dl_button.click() #download the file
            


'''
//*[@id="search-results"]/tbody/tr[1]/td[3]/a
//*[@id="search-results"]/tbody/tr[7]/td[3]/a
//*[@id="search-results"]/tbody/tr[8]/td[3]/a
//*[@id="search-results"]/tbody/tr[20]/td[3]/a

/html/body/div[2]/div[3]/nav/div/div/ul/li[8]/a
'''