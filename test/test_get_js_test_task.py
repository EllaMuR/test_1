import fixture.api_req



def test_get_products(api_client):
    products = fixture.api_req.get_js_test_task(api_client)
    assert fixture.api_req.compare_product_names(products) == True
    assert sorted(products) == products