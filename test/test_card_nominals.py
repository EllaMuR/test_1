import time
def test_card_nominals(app):

    c = app.card_noms.find_card_noms_quantity()
    # app.card_noms.click_on_card_noms()
    # card_value= app.card_noms.get_nominal_value()
    print(c)
    # print(card_value)
    for id in range(1, (c+1)):

        card_nom = app.card_noms.get_button_value(id)
        time.sleep(2)
        card_value = app.card_noms.get_nominal_value()
        print("1"+str(card_nom)+" "+str(card_value))
        assert card_nom == card_value