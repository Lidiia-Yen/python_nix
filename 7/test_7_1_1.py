import pytest
# from hamcrest import *
# can't import this module
from selectors_and_methods import Order
import json


form = {'comments': 'Nauky Prospect, 11/22',
        'custemail': 'test@gmail.com',
        'custname': 'Lidia Yen',
        'custtel': '911',
        'delivery': '11:00',
        'size': 'medium',
        'topping': ['bacon', 'mushroom']}


@pytest.mark.order_pizza
def test_order(chrome_driver,):
    page = Order(chrome_driver)
    page.go_to_site()
    page.fill_fields(name=form['custname'], tel_number=form['custtel'], email=form['custemail'],
                     delivery_time='11:00am', comment=form['comments'])
    page.select_size(form['size'])
    page.select_topping(form['topping'])
    page.click_submit()
    assert json.loads(page.json_response().text)['form'] == form
