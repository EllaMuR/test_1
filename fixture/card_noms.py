import time

from selenium.webdriver.common.action_chains import ActionChains
class Card_Noms:
    def __init__(self, app):
        self.app = app

    def find_card_noms_quantity(self):
        wd = self.app.wd
        return len(wd.find_elements_by_class_name("par-options__button"))


    def click_on_card_noms(self, index):
        wd = self.app.wd
        wd.execute_script("window.scrollBy(0, 800)")
        wd.find_element_by_xpath("//li[%s]/button" %index).click()
        time.sleep(2)


    def get_button_value(self, index):
        self.click_on_card_noms(index)
        # c = self.is_button_active()
        # print(str(c))
        wd = self.app.wd
        return wd.find_element_by_xpath("//li[%s]/button" %index).text

    def get_nominal_value(self):
        wd = self.app.wd
        return wd.find_element_by_id("range-value-input").get_attribute('value')


    # def is_button_active(self):
    #     wd = self.app.wd
    #     res = wd.find_elements_by_class_name("button--active").get_attribute('value')
    #     return res
    #     #assert res == self.get_button_value(index)