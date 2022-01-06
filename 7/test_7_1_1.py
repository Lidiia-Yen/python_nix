# from hamcrest import *
import pytest
from selectors_and_methods import Order
import json


form = {"comments": "Nauky Prospect, 11/22",
                   "custemail": "yenlidiya@gmail.com",
                   "custname": "Lidia Yen",
                   "custtel": "911",
                   "delivery": "",
                   "size": "medium",
                   "topping": "bacon"}


@pytest.mark.order_pizza
def test_order(chrome_driver):
    page = Order(chrome_driver)
    page.go_to_site()
    page.enter_name("Lidia Yen")
    page.enter_tel("911")
    page.enter_email("yenlidiya@gmail.com")
    page.select_bacon()
    # page.select_cheese()
    # page.select_onion()
    page.select_medium()
    page.enter_comment("Nauky Prospect, 11/22")
    page.click_submit()
    assert(json.loads(page.json_response().text)['form'] == form)
