import unittest
from data_validator import *

# Author: Vaishali Patel
class DataValidatorTests(unittest.TestCase):
    
	@classmethod
    def setUpClass(cls):
        cls.dataValidator = DataValidator()

    def setUp(self):
        # be executed before each test
        print("set up")
        self.data = [['A011', 'M', '29', '458', 'Normal', '20', '05-03-1999'],
                     ['C224', 'F', '7', '679', 'Overweight', '240', '12-1-1978'],
                     ['E3', 'Male', 'seven', '99,9', 'obesity', '6,00', '2-11-19']]

        self.data_2 = [['E001', 'F', '20', '350', 'Normal', '200', '20-09-1998']]

        self.data_3 = [['', '', '', '', '', '', '']]

        self.data_4 = [['F001', 'Female', 'eight', '4oo', 'Overweight', '280', '30-06-2000']]

        self.data_5 = [['@000', '*', '^', '&%&', '_', '$', '?-05-?']]

    def tearDown(self):
        # be executed after each test case
        print("teardown")

	# Test 1
    def test_data_validator_01(self):
        # good day for testing validator
        result = [['E001', 'F', '19', '220', 'Normal', '290', '03-10-2000']]
        self.assertEqual(self.dataValidator.validate_data(self.data_2), result, "That is a valid data array")
	
	# Test 2
    def test_data_validator_02(self):
        # bad day for testing validator no data
        result = []
        self.assertEqual(self.dataValidator.validate_data(self.data_3), result, "That is not a valid data array")

	# Test 3	
    def test_data_validator_03(self):
        # bad day for testing validator some data
        result = []
        self.assertEqual(self.dataValidator.validate_data(self.data_4), result, "That is not a valid data array")

	# Test 4
    def test_data_validator_04(self):
        # bad day for testing validator can it handle special characters
        result = []
        self.assertEqual(self.dataValidator.validate_data(self.data_5), result, "That is not a valid data array")

	# Testing valid empid input
	# Test 5
    def test_person_empid_01(self):
        empid = self.data[0][0]
        self.assertTrue(self.dataValidator.validate_empid(empid), "This is a valid EmployeeID input")

	# Test 6	
    def test_person_empid_02(self):
        empid = self.data[1][0]
        self.assertTrue(self.dataValidator.validate_empid(empid), "This is a valid EmployeeID input")

	# Test 7
    def test_person_empid_03(self):
        empid = self.data[2][0]
        self.assertFalse(self.dataValidator.validate_empid(empid), "This is  NOT a valid EmployeeID input")

	# Test 8
	def test_person_age_01(self):
        # good day test for person 1
        age = self.data[0][2]
        self.assertTrue(self.dataValidator.validate_age(age), "That is not a valid age input")

	# Test 9
    def test_person_age_02(self):
        # good day test for person 2
        age = self.data[1][2]
        self.assertFalse(self.dataValidator.validate_age(age), "That is not a valid age input")

	# Test 10
    def test_person_age_03(self):
        # bad day test for person 3 bad data is rejected
        age = self.data[2][2]
        self.assertFalse(self.dataValidator.validate_age(age), "That is not a valid age input")

    # Testing valid gender input
    # Test 11
	def test_person_gender_01(self):
        gender = self.data[0][1]
        self.assertTrue(self.dataValidator.validate_gender(gender), "This is a valid Gender input")

	 # Test 12
    def test_person_gender_02(self):
        gender = self.data[1][1]
        self.assertTrue(self.dataValidator.validate_gender(gender), "This is a valid Gender input")

	# Test 13
    def test_person_gender_03(self):
        gender = self.data[2][2]
        self.assertFalse(self.dataValidator.validate_gender(gender), "This is NOT a valid Gender input")

    # Testing valid sales
	# Test 14
    def test_person_sales_01(self):
        sales = self.data[0][3]
        self.assertTrue(self.dataValidator.validate_sales(sales), "This is a valid Sales input")

	# Test 15
    def test_person_sales_02(self):
        sales = self.data[1][3]
        self.assertTrue(self.dataValidator.validate_sales(sales), "This is a valid Sales input")
	
	# Test 16
    def test_person_sales_03(self):
        sales = self.data[2][3]
        self.assertFalse(self.dataValidator.validate_sales(sales), "This is NOT a valid Sales input")

    # Testing valid BMI input
	 # Test 17
    def test_person_bmi_01(self):
        bmi = self.data[0][4]
        self.assertTrue(self.dataValidator.validate_bmi(bmi), "This is a valid BMI input")
 
	# Test 18
    def test_person_bmi_02(self):
        bmi = self.data[1][4]
        self.assertTrue(self.dataValidator.validate_bmi(bmi), "This is a valid BMI input")

	# Test 19
    def test_person_bmi_03(self):
        bmi = self.data[2][4]
        self.assertFalse(self.dataValidator.validate_bmi(bmi), "This is NOT a valid BMI input")

	# Test 20
    # Testing valid Salary input
    def test_person_salary_01(self):
        salary = self.data[0][5]
        self.assertTrue(self.dataValidator.validate_salary(salary), "This is a valid Salary input")
	
	# Test 21
    def test_person_salary_02(self):
        salary = self.data[1][5]
        self.assertTrue(self.dataValidator.validate_salary(salary), "This is a valid Salary input")
	
	# Test 22
    def test_person_salary_03(self):
        salary = self.data[2][5]
        self.assertFalse(self.dataValidator.validate_salary(salary), "This is NOT a valid Salary input")

    # Testing valid Birthdate input
	# Test 23
    def test_person_birthday_01(self):
        birthday = self.data[0][6]
        self.assertTrue(self.dataValidator.validate_birthday(birthday), "This is a valid Birthday input")

	# Test 24
    def test_person_birthday_02(self):
        birthday = self.data[1][6]
        self.assertTrue(self.dataValidator.validate_birthday(birthday), "This is a valid Birthday input")
	
	# Test 25
    def test_person_birthday_03(self):
        birthday = self.data[2][6]
        self.assertFalse(self.dataValidator.validate_birthday(birthday), "This is NOT a valid Birthday input")

if __name__ == '__main__':
    unittest.main()
