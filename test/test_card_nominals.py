import time

import allure
import pytest

def test_card_nominals(app):
    with allure.step('Finding quantity of card nominals:'):
        c = app.card_noms.find_card_noms_quantity()
        #print(c)
    for id in range(1, (c+1)):
        with allure.step(f"Finding selected card value:{id}"):
            card_nom = app.card_noms.get_button_value(id)
        with allure.step(f"Finding is button active:{id}"):
            assert card_nom == app.card_noms.is_button_active()
            time.sleep(2)
        with allure.step(f"Getting selected card value from nominal field: {id}"):
            card_value = app.card_noms.get_nominal_value()
            #print(str(card_nom)+" "+str(card_value))
        with allure.step(f"Comparing selected card values from button and nominal field: {id}"):
            assert card_nom == card_value