import pytest
from selenium import webdriver


def pytest_configure(config):
    config.addinivalue_line('markers', 'order_pizza')


# @pytest.fixture(scope='session')
# def chrome_driver():
#     driver = webdriver.Chrome('chromedriver.exe')
#     yield driver
#     driver.quit()
