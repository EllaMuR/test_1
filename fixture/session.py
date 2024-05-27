import time

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        base_url = self.app.config['web']['baseUrl']
        wd = self.app.wd
        wd.get("http://"+username+":"+password+"@"+base_url)
        time.sleep(1)
        wd.execute_script("window.scrollBy(0, 800)")
