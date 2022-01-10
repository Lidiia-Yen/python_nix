from base_actions import BaseActions
from selenium.webdriver.common.by import By


class FormLocators:
    locator_name_input = (By.NAME, 'custname')
    locator_tel_input = (By.NAME, 'custtel')
    locator_email_input = (By.NAME, 'custemail')
    locator_small_radiobutton = (By.XPATH, '//input[@type = "radio" and @value="small"]')
    locator_medium_radiobutton = (By.XPATH, '//input[@type = "radio" and @value="medium"]')
    locator_large_radiobutton = (By.XPATH, '//input[@type = "radio" and @value="large"]')
    locator_bacon_checkbox = (By.XPATH, '//input[@type = "checkbox" and @value="bacon"]')
    locator_cheese_checkbox = (By.XPATH, '//input[@type = "checkbox" and @value="cheese"]')
    locator_onion_checkbox = (By.XPATH, '//input[@type = "checkbox" and @value="onion"]')
    locator_mushroom_checkbox = (By.XPATH, '//input[@type = "checkbox" and @value="mushroom"]')
    locator_delivery_input = (By.NAME, 'delivery')
    locator_comment_input = (By.NAME, 'comments')
    locator_submit_button = (By.XPATH, '//button')
    locator_json_response = (By.XPATH, '//pre')


class Order(BaseActions):

    def fill_fields(self, name, tel_number, email, comment, delivery_time):
        name_field = self.find_element(FormLocators.locator_name_input)
        name_field.click()
        name_field.send_keys(name)
        tel_field = self.find_element(FormLocators.locator_tel_input)
        tel_field.click()
        tel_field.send_keys(tel_number)
        email_field = self.find_element(FormLocators.locator_email_input)
        email_field.click()
        email_field.send_keys(email)
        delivery_field = self.find_element(FormLocators.locator_delivery_input)
        delivery_field.click()
        delivery_field.send_keys(delivery_time)
        comment_field = self.find_element(FormLocators.locator_comment_input)
        comment_field.click()
        comment_field.send_keys(comment)
        return name_field, tel_field, email_field, delivery_field, comment_field

    def select_size(self, size):
        if size == 'small':
            size = self.find_element(FormLocators.locator_small_radiobutton)
            return size.click()
        elif size == 'medium':
            size = self.find_element(FormLocators.locator_medium_radiobutton)
            return size.click()
        elif size == 'large':
            size = self.find_element(FormLocators.locator_large_radiobutton)
            return size.click()

    def select_topping(self, *kwargs):
        topping = []
        if 'bacon' in kwargs:
            check_box_1 = self.find_element(FormLocators.locator_bacon_checkbox)
            check_box_1.click()
            topping.append(check_box_1)
        if 'cheese' in kwargs:
            check_box_2 = self.find_element(FormLocators.locator_cheese_checkbox)
            check_box_2.click()
            topping.append(check_box_2)
        if 'onion' in kwargs:
            check_box_3 = self.find_element(FormLocators.locator_onion_checkbox)
            check_box_3.click()
            topping.append(check_box_3)
        if 'mushroom' in kwargs:
            check_box_4 = self.find_element(FormLocators.locator_mushroom_checkbox)
            check_box_4.click()
            topping.append(check_box_4)
        return topping

    def click_submit(self):
        return self.find_element(FormLocators.locator_submit_button).click()

    def json_response(self):
        json_text = self.find_elements(FormLocators.locator_json_response)
        return json_text
