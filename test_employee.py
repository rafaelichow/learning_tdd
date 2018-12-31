import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee('Rafael', 'Chow', 10000)
        self.emp2 = Employee('Rafael', 'Klein', 9000)
        self.emp3 = Employee('Rafael', 'Inaimo', 11000)

    def test_email(self):
        self.assertEqual(self.emp1.email, 'rafaelchow@domain.com')
        self.assertEqual(self.emp2.email, 'rafaelklein@domain.com')
        self.assertEqual(self.emp3.email, 'rafaelinaimo@domain.com')

        self.emp1.first = 'Alexandre'
        self.emp2.first = 'Roberto'
        self.emp3.last = 'Amaral'

        self.assertEqual(self.emp1.email, 'alexandrechow@domain.com')
        self.assertEqual(self.emp2.email, 'robertoklein@domain.com')
        self.assertEqual(self.emp3.email, 'rafaelamaral@domain.com')

    def test_full_name(self):
        self.assertEqual(self.emp1.full_name, 'Rafael Chow')
        self.assertEqual(self.emp2.full_name, 'Rafael Klein')
        self.assertEqual(self.emp3.full_name, 'Rafael Inaimo')

        self.emp1.first = 'Alexandre'
        self.emp2.first = 'Roberto'
        self.emp3.last = 'Amaral'

        self.assertEqual(self.emp1.full_name, 'Alexandre Chow')
        self.assertEqual(self.emp2.full_name, 'Roberto Klein')
        self.assertEqual(self.emp3.full_name, 'Rafael Amaral')

    def test_raise(self):
        self.emp1.apply_raise()
        self.emp2.apply_raise()
        self.emp3.apply_raise()

        self.assertEqual(self.emp1.pay, 10500)
        self.assertEqual(self.emp2.pay, 9450)
        self.assertEqual(self.emp3.pay, 11550)

if __name__ == '__main__':
    unittest.main()
