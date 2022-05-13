from page_objects import PageObject, PageElement


class OrderForm(PageObject):
    name = PageElement(xpath='//input[@name="custname"]')
    tel = PageElement(xpath='//input[@name="custtel"]')
    email = PageElement(xpath='//input[@name="custemail"]')
    delivery = PageElement(name='delivery')
    comment = PageElement(name='comments')
    submit = PageElement(xpath='//button')
    json_response = PageElement(xpath='//pre')
