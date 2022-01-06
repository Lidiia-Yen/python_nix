from page_objects import PageObject, PageElement
from base_actions import BasePageActions
import pytest
import json


class OrderPage(PageObject):
    name_input = PageElement(xpath='//input[@name="custname"]')
    tel_input = PageElement(xpath='//input[@name="custtel"]')
    email_input = PageElement(xpath='//input[@name="custemail"]')
    small_radiobutton = PageElement(xpath='//input[@type = "radio" and @value="small"]')
    medium_radiobutton = PageElement(xpath='//input[@type = "radio" and @value="medium"]')
    large_radiobutton = PageElement(xpath='//input[@type = "radio" and @value="large"]')
    bacon_checkbox = PageElement(xpath='//input[@type = "checkbox" and @value="bacon"]')
    cheese_checkbox = PageElement(xpath='//input[@type = "checkbox" and @value="cheese"]')
    onion_checkbox = PageElement(xpath='//input[@type = "checkbox" and @value="onion"]')
    mushroom_checkbox = PageElement(xpath='//input[@type = "checkbox" and @value="mushroom"]')
    # time_input = PageElement(xpath='//input[@name="delivery"]')
    comment_input = PageElement(xpath='//input[@name="comments"]')
    submit_button = PageElement(xpath='//button')
    json_response = PageElement(xpath='//pre')


class Order(BasePageActions):

    def enter_name(self, name):
        field = self.find_element(OrderPage.name_input)
        field.click()
        field.send_keys(name)
        return field

    def enter_tel(self, telephone_number):
        field = self.find_element(OrderPage.tel_input)
        field.click()
        field.send_keys(telephone_number)
        return field

    def enter_email(self, email):
        field = self.find_element(OrderPage.email_input)
        field.click()
        field.send_keys(email)
        return field

    def select_small(self):
        size = self.find_element(OrderPage.small_radiobutton)
        size.click()
        return size

    def select_medium(self):
        size = self.find_element(OrderPage.medium_radiobutton)
        size.click()
        return size

    def select_large(self):
        size = self.find_element(OrderPage.small_radiobutton)
        size.click()
        return size

    def select_bacon(self):
        topping = self.find_element(OrderPage.bacon_checkbox)
        topping.click()
        return topping

    def select_cheese(self):
        topping = self.find_element(OrderPage.cheese_checkbox)
        topping.click()
        return topping

    def select_onion(self):
        topping = self.find_element(OrderPage.onion_checkbox)
        topping.click()
        return topping

    def select_mushroom(self):
        topping = self.find_element(OrderPage.mushroom_checkbox)
        topping.click()
        return topping

    def enter_comment(self, text):
        field = self.find_element(OrderPage.comment_input)
        field.click()
        field.send_keys(text)
        return field

    def click_submit(self):
        return self.find_element(OrderPage.submit_button).click()

    def json_response(self):
        json_text = self.find_elements(OrderPage.json_response)
        return json_text
