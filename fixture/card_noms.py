from selenium.webdriver.common.by import By

class Card_Noms:
    def __init__(self, app):
        self.app = app

    def find_card_noms_quantity(self):
        """Поиск количества кнопок с номиналом"""
        wd = self.app.wd
        return len(wd.find_elements_by_class_name("par-options__button"))


    def click_on_card_noms(self, index):
        """Клик по кнопке с номиналом
        index - индекс/номер кнопки"""
        wd = self.app.wd
        #wd.find_element_by_xpath("//li[%s]/button" %index).click()
        wd.find_element(By.XPATH, "//li[%s]/button" %index).click()


    def get_button_value(self, index):
        """Получение значения номинала у кнопки
        index - индекс/номер кнопки
        возвращается - текст с номиналом"""
        self.click_on_card_noms(index)
        wd = self.app.wd
        #return wd.find_element_by_xpath("//li[%s]/button" %index).text
        return wd.find_element(By.XPATH, "//li[%s]/button" %index).text

    def get_nominal_value(self):
        """Получение значения номинала у поля ввода"""
        wd = self.app.wd
        #return wd.find_element_by_id("range-value-input").get_attribute('value')
        return wd.find_element(By.ID, "range-value-input").get_attribute('value')


    def is_button_active(self):
        """Проверка, что выбранная кнопка становится активной"""
        wd = self.app.wd
        #res = (wd.find_element_by_class_name("par-options__button--active").text)
        res = (wd.find_element(By.CLASS_NAME, "par-options__button--active").text)
        return res
