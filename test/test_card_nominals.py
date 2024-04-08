import time
def test_card_nominals(app):
    c = app.card_noms.find_card_noms_quantity()
    print(c)
    for id in range(1, (c+1)):
        card_nom = app.card_noms.get_button_value(id)
        assert card_nom == app.card_noms.is_button_active()
        time.sleep(2)
        card_value = app.card_noms.get_nominal_value()
        print(str(card_nom)+" "+str(card_value))
        assert card_nom == card_value