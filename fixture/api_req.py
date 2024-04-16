import time
from Model.JsTestTask import JsTestTask


class apiHelper:

    def __init__(self, app):
        self.app = app

    def get_js_test_task(self, api_client):
        #получение списка продуктов
        base_url = self.app.config['api']['baseUrl']
        url = base_url+"/api/js-test-task/"
        list = []
        page = 1
        params = {
            'search': 'Alcatel',
            'sort_field': 'name',
            'page': str(page)
        }
        r = api_client.get(url, params=params)
        time.sleep(1)
        #breakpoint()
        #status = self.assert_status_code(r)
        status=r.status_code
        print(str(status))
        #breakpoint()
        data = r.json()
        #breakpoint()
        if status == 200:
            while data['next_page_url']:
                for i in data['products']:
                    print(i)
                    list.append(i)
                #breakpoint()
                page += 1
                params['page'] = str(page)
                r = api_client.get(url, params=params)
                time.sleep(1)
                status = r.status_code
                print(str(status))
                #breakpoint()
                if status == 200:
                    data = r.json()
                    #breakpoint()
            if not data['next_page_url']:
                #breakpoint()
                for i in data['products']:
                    list.append(i)
                    print(i)
            l = len(list)
            print(str(l))
            products = [JsTestTask(**i) for i in list]
            return products
        else:
            print("Запрос со статус-кодом:", str(status))

    # def assert_status_code(self, req):
    #   #сравнение статус-кода с ОК
    #     #print(req.status_code)
    #     if req.status_code == 200:
    #         return True
    #     else:
    #         return False


    def compare_product_names(self, products):
        #сравнение полученного списка с требуемым параметром
        for product in products:
            if "Alcatel" in product.name:
                return True
            else:
                return False




