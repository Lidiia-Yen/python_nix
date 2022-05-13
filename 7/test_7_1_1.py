import pytest
from hamcrest import assert_that, equal_to
from steps import PopulateOrder
from config import ORDER_DATA, ORDER_FORM_URL

# pytest -v  7/test_7_1_1.py


@pytest.mark.order_pizza
@pytest.mark.parametrize('test', [ORDER_DATA])
def test_order(test):
    response = PopulateOrder(ORDER_FORM_URL).populate_order(test)['form']
    for key in response:
        assert_that(response[key], equal_to(ORDER_DATA[key]), 'form_response is not equal to sent data')
