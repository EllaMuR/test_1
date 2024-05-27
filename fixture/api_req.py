import re
import time
from Model.JsTestTask import JsTestTask


def get_js_test_task(api_client):
    """Получение списка позиций и запись в класс"""
    base_url="https://www.lenvendo.ru/api/js-test-task/"
    list = []
    page = 1
    params = {
        'search': 'Alcatel',
        'sort_field': 'name',
        'page': str(page)
    }
    r = api_client.get(base_url, params=params)
    time.sleep(1)
    data = r.json()
    while data['next_page_url']:
        for i in data['products']:
            print(i)
            list.append(i)
        page += 1
        params['page'] = str(page)
        r = api_client.get(base_url, params=params)
        data = r.json()
    if not data['next_page_url']:
        for i in data['products']:
            list.append(i)
            print(i)
    print(str(len(list)))
    products = [JsTestTask(**i) for i in list]
    return products


def compare_product_names(products):
    """Проверка того, что полученный список соответствует требуемому параметру"""
    for product in products:
        match=re.search('Alcatel', product.name)
        if not match:
            return False
    return True




