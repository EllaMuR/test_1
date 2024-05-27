from selenium import webdriver
from fixture.session import SessionHelper
from fixture.card_noms import Card_Noms


class Application:
    def __init__(self, browser, config):
        if browser == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser == "Chrome":
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
        self.session = SessionHelper(self)
        self.card_noms = Card_Noms(self)
        self.config = config
        self.base_url = config['web']['baseUrl']


    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
