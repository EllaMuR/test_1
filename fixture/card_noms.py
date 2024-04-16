import time

from selenium.webdriver.common.action_chains import ActionChains
class Card_Noms:
    def __init__(self, app):
        self.app = app

    def find_card_noms_quantity(self):
        #количество кнопок с номиналом
        wd = self.app.wd
        return len(wd.find_elements_by_class_name("par-options__button"))


    def click_on_card_noms(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[%s]/button" %index).click()
        #time.sleep(2)


    def get_button_value(self, index):
        #получение значения кнопки
        self.click_on_card_noms(index)
        wd = self.app.wd
        return wd.find_element_by_xpath("//li[%s]/button" %index).text

    def get_nominal_value(self):
        #получение значения поля ввода
        wd = self.app.wd
        return wd.find_element_by_id("range-value-input").get_attribute('value')


    def is_button_active(self):
        #проверка на значение активной кнопки
        wd = self.app.wd
        res = (wd.find_element_by_class_name("par-options__button--active").text)
        return res
