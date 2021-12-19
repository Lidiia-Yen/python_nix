from zeep import Client
client = Client(wsdl='http://secure.smartbearsoftware.com/samples/testcomplete10/webservices/Service.asmx?WSDL')

# task_1
def modify_object():
    client.transport.session.headers.update({'User-Agent': 'Python Learning Requests'})
    get_object = client.service.GetSampleObject(no=3)
    get_object['X'], get_object['Y'] = get_object['Y'], get_object['X']
    get_object['Name'] = 'My Test'
    return f'\n Task 1: {client.service.SetSampleObject(get_object)}'


# task_2
def get_books():
    client.transport.session.headers.update({'User-Agent': 'Python Learning Requests'})
    get_lxml = client.service.GetXmlData()
    all_books = get_lxml.findall('book')
    books = {}
    for book in all_books:
        book_attributes = {}
        tags = ['id', 'title', 'genre', 'review', 'price']
        for items in book:
            if items.tag in tags:
                book_attributes[items.tag] = items.text
        books[book.get('id')] = book_attributes
    return f'\n Task 2: {books}'


if __name__ == "__main__":
    print(modify_object())
    print(get_books())
