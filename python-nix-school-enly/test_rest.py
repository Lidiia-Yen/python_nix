import unittest
import rest_511


class TestRest(unittest.TestCase):
    def setUp(self):
        self.get_not_200 = rest_511.get_not200()
        self.submit_an_order = rest_511.submit_order()
        self.find_all_countries = rest_511.find_countries()

    # task_1
    def test_not200_result(self):
        self.assertNotEqual(len(self.get_not_200), 0, "only status codes 200 are returned, no other status codes")

    # task_2
    def test_response_type(self):
        self.assertNotEqual(type(self.submit_an_order[0]), Exception)

    def test_user_agent(self):
        self.assertIn('User-Agent', self.submit_an_order[1].keys())

    def test_customer_name(self):
        self.assertEqual(len(self.submit_an_order[0]['custname'].split(' ')), 2)

    def test_customer_email(self):
        self.assertIn('@', self.submit_an_order[0]['custemail'])

    # task_3_1/3_2
    def test_languages_return(self):
        self.assertIn('languages', self.find_all_countries[0].keys())


if __name__ == '__main__':
    unittest.main()
