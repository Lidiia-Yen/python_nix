from page_elements import OrderForm
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


class PopulateOrder:

    def __init__(self, url):
        self.driver = webdriver.Chrome('chromedriver.exe')
        if url:
            self.driver.get(url)
            self.page = OrderForm(self.driver)

    def select_size(self, size):
        self.driver.find_element(By.XPATH, f'//input[@type = "radio" and @value="{size}"]').click()

    def select_topping(self, toppings):
        for topping in toppings:
            self.driver.find_element(By.XPATH, f'//input[@type = "checkbox" and @value="{topping}"]').click()

    def populate_order(self, data):
        self.page.name = data['custname']
        self.page.tel = data['custtel']
        self.page.email = data['custemail']
        self.select_size(data['size'])
        self.select_topping(data['topping'])
        self.page.delivery = f"{data['delivery']}am"
        self.page.comment.send_keys(data['comments'])
        self.page.submit.click()
        return json.loads(self.page.json_response.text)
