import fixture.api_req
from Model.JsTestTask import JsTestTask


def test_get_products(app, api_client):
    #breakpoint()
    products = app.apiHelper.get_js_test_task(api_client)
    #breakpoint()
    assert app.apiHelper.compare_product_names(products) == True
    # breakpoint()
    assert sorted(products) == products