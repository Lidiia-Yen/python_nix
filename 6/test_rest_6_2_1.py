import unittest
from unittest import expectedFailure

from rest_soap5 import rest_5_1_1


class TestRest(unittest.TestCase):
    def setUp(self):
        self.get_not_200 = rest_5_1_1.get_not200()
        self.submit_an_order = rest_5_1_1.submit_order()
        self.get_languages = rest_5_1_1.get_all_languages()
        self.get_population = rest_5_1_1.get_lang_population(lang_codes=['eng', 'rus', 'fra', 'spa', 'zho'])

    # task_1
    def test_not200_result(self):
        self.assertNotEqual(len(self.get_not_200), 0, "only status codes 200 are returned, no other status codes")

    # task_2
    def test_response_type(self):
        self.assertNotEqual(type(self.submit_an_order[0]), Exception)

    def test_customer_name(self):
        self.assertEqual(len(self.submit_an_order[0]['custname'].split(' ')), 2)

    def test_customer_email(self):
        self.assertIn('@', self.submit_an_order[0]['custemail'])

    # task_3_1/3_2
    def test_languages_return(self):
        self.assertIn('eng', self.get_languages)

    def test_get_population(self):
        self.assertIn('eng', self.get_population.keys())


if __name__ == '__main__':
    unittest.main()
