import unittest
from data_validator import DataValidator


class TestDataValidator(unittest.TestCase):
    def setUp(self):
        self.vld = DataValidator()

    def test_invalid_empid(self):
        data = ['A0011', 'F', '21', '001', 'Normal', '12', '1-1-1996']
        result = [None, 'F', '21', '001', 'Normal', '012', '01-01-1996']
        self.assertEqual(self.vld.check_all(data), result)

    def test_invalid_gender(self):
        data = ['A001', '222', '21', '001', 'Normal', '12', '1-1-1996']
        result = ['A001', None, '21', '001', 'Normal', '012', '01-01-1996']
        self.assertEqual(self.vld.check_all(data), result)

    def test_valid_gender_01(self):
        data = ['A001', 'girl', '21', '001', 'Normal', '12', '1-1-1996']
        result = ['A001', 'F', '21', '001', 'Normal', '012', '01-01-1996']
        self.assertEqual(self.vld.check_all(data), result)

    def test_invalid_age(self):
        data = ['A001', 'M', '101', '001', 'Normal', '12', '1-1-1996']
        result = ['A001', 'M', None, '001', 'Normal', '012', '01-01-1996']
        self.assertEqual(self.vld.check_all(data), result)

    def test_invalid_sales(self):
        data = ['A001', 'M', '21', 'abc', 'Normal', '12', '1-1-1996']
        result = ['A001', 'M', '21', None, 'Normal', '012', '01-01-1996']
        self.assertEqual(self.vld.check_all(data), result)

    def test_invalid_bmi(self):
        data = ['A001', 'M', '21', '001', 'Thin', '12', '1-1-1996']
        result = ['A001', 'M', '21', '001', None, '012', '01-01-1996']
        self.assertEqual(self.vld.check_all(data), result)

    def test_invalid_salary(self):
        data = ['A001', 'M', '21', '001', 'Normal', '1', '1-1-1996']
        result = ['A001', 'M', '21', '001', 'Normal', None, '01-01-1996']
        self.assertEqual(self.vld.check_all(data), result)

    def test_invalid_birthday_01(self):
        data = ['A001', 'M', '21', '001', 'Normal', '12', '31-2-1996']
        self.assertRaises(ValueError, self.vld.check_all, data)

    def test_invalid_birthday_02(self):
        data = ['A001', 'M', '21', '001', 'Normal', '12', '15-May-1996']
        result = ['A001', 'M', '21', '001', 'Normal', '012', None]
        self.assertEqual(self.vld.check_all(data), result)

    def test_invalid_values(self):
        data = ['A001', 'M', '21', '001', 'Normal', '12']
        self.assertEqual(self.vld.check_all(data), [])

    def test_valid_values(self):
        data = ['A001', 'M', '21', '001', 'Normal', '12', '1-1-1996']
        result = ['A001', 'M', '21', '001', 'Normal', '012', '01-01-1996']
        self.assertEqual(self.vld.check_all(data), result)


if __name__ == '__main__':  # pragma: no cover
    unittest.main(verbosity=2)  # pragma: no cover
