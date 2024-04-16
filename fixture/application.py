
# noinspection PyInterpreter
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.card_noms import Card_Noms
from fixture.api_req import apiHelper
from selenium.webdriver.common.action_chains import ActionChains

class Application:
    def __init__(self, browser, config):#, username, password
        if browser == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser == "Chrome":
            self.wd = webdriver.Chrome()

        else:
            raise ValueError("Unrecognised browser %s" % browser)
#       self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.card_noms = Card_Noms(self)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.apiHelper = apiHelper(self)



    # def open_homepage(self):
    #     wd = self.wd
    #     wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
