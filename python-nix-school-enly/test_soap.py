import unittest
import soap_5_2_1


class TestSoap(unittest.TestCase):
    def setUp(self):
        self.modify_object = soap_5_2_1.modify_object()
        self.get_all_books = soap_5_2_1.get_books()

    # task_1
    def test_object_name(self):
        self.assertEqual(self.modify_object.split(';')[0], 'Name = My Test')

    # task_2
    def test_there_are_books(self):
        self.assertNotEqual(len(self.get_all_books.keys()), 0)

    def test_if_have_price(self):
        self.assertIn('price', self.get_all_books['bk001'].keys())


if __name__ == '__main__':
    unittest.main()
