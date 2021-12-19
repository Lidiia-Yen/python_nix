import unittest
import rest_511


class Test1(unittest.TestCase):
    def setUp(self):
        self.get_not_200 = rest_511.get_not200()
        self.submit_an_order = rest_511.submit_order()

    def test_modify_object(self):
        self.assertNotEqual(len(self.get_not_200), 0, "only status codes 200 are returned, no other status codes")

    def test_content_type(self):
        self.assertEqual(self.submit_an_order[1]['Content-Type'], 'application/json')

    def test_response_type(self):
        self.assertNotEqual(type(self.submit_an_order[0]), Exception)






if __name__ == '__main__':
    unittest.main()
