import pytest
# from hamcrest import *
# can't import this module
from selectors_and_methods import Order
import json


@pytest.mark.parametrize('test_name', ['Lidia Yen'])
@pytest.mark.parametrize('test_tel', ['911'])
@pytest.mark.parametrize('test_email', ['test@gmail.com'])
@pytest.mark.parametrize('test_size', ['medium'])
@pytest.mark.parametrize('test_topping', [('bacon', 'mushroom')])
@pytest.mark.parametrize('test_delivery', ['11:00am'])
@pytest.mark.parametrize('test_comments', ['Nauky 11/4'])
@pytest.mark.order_pizza
def test_order(chrome_driver, test_name, test_tel, test_email, test_size, test_topping, test_delivery, test_comments):
    page = Order(chrome_driver)
    page.go_to_site()
    page.fill_fields(name=test_name, tel_number=test_tel, email=test_email, delivery_time=test_delivery,
                     comment=test_comments)
    expected_form = {'comments': 'Nauky 11/4',
                     'custemail': 'test@gmail.com',
                     'custname': 'Lidia Yen',
                     'custtel': '911',
                     'delivery': '11:00',
                     'size': 'medium',
                     'topping': ['bacon', 'mushroom']}
    page.select_size(test_size)
    page.select_topping(test_topping)
    page.click_submit()
    assert json.loads(page.json_response().text)['form'] == expected_form
