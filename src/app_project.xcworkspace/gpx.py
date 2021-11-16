from selenium import webdriver
import time
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

        return None