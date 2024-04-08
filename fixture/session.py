import time
import requests
from requests.auth import HTTPDigestAuth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        base_url = self.app.config['web']['baseUrl']
        wd = self.app.wd
        wd.get("http://"+username+":"+password+"@"+base_url)
        time.sleep(2)
        # self.app.open_homepage()

        # WebDriverWait(wd, 10).until(EC.alert_is_present())
        # username=self.app.config['login_info']['username']
        # password=self.app.config['login_info']['password']
        # wd.switch_to.alert.send_keys("HR"+Keys.TAB+"test")
        # wd.switch_to.alert.accept()
        # requests.get("https://qa.digift.ru/", auth=HTTPDigestAuth("HR", "test"))
        # wd.find_element_by_name("username").click()
        # wd.find_element_by_name("username").clear()
        # wd.find_element_by_name("username").send_keys(username)
        # wd.find_element_by_name("password").click()
        # wd.find_element_by_name("password").clear()
        # wd.find_element_by_name("password").send_keys(password)
        # wd.find_element_by_css_selector('input[type="submit"]').click()


    # def logout(self):
    #     wd = self.app.wd
    #     time.sleep(1)
    #     wd.find_element_by_link_text("Logout").click()
    #     time.sleep(1)

    # def ensure_logout(self):
    #     wd = self.app.wd
    #     if self.is_logged_in():
    #         self.logout()

    # def is_logged_in(self):
    #     wd = self.app.wd
    #     return len(wd.find_elements_by_link_text("Logout")) > 0

    # def is_logged_in_as(self, username):
    #     wd = self.app.wd
    #     return self.get_logged_user() == username

    # def get_logged_user(self):
    #     wd = self.app.wd
    #     return wd.find_element_by_css_selector("td.login-info-left span").text


    # def ensure_login(self, username, password):
    #     wd = self.app.wd
    #     if self.is_logged_in():
    #         if self.is_logged_in_as(username):
    #             return
    #         else:
    #             self.logout()
    #     self.login(username, password)