from zeep import Client

# Task_1
wsdl = 'http://secure.smartbearsoftware.com/samples/testcomplete10/webservices/Service.asmx?WSDL'
client = Client(wsdl=wsdl)
service = client.bind(service_name='SampleWebService', port_name='SampleWebServiceSoap')

my_object_x = service.GetSampleObject(no=3)['Y']
my_object_y = service.GetSampleObject(no=3)['X']
my_object = service.SetSampleObject({"no": 3, "X": my_object_x, "Y": my_object_y, "Name": "My Test"})


print(service.GetSampleObject(no=3))

# python -mzeep http://secure.smartbearsoftware.com/samples/testcomplete10/webservices/Service.asmx?WSDL
# client.transport.session.headers.update({'User-Agent': 'Python Learning Requests'})