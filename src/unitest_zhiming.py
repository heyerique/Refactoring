from unittest import TestCase, main
from csv_operations import CSVOperations
from data import Data
from data_validator import DataValidator
from staff_data import StaffData


class MainTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        csv = CSVOperations("staffinfo.csv")
        self.assertTrue(type(csv._fieldnames) == list)

    def test_02(self):
        csv = CSVOperations("staffinfo.csv")
        items = ["EMPID", "GENDER", "AGE", "SALES", "BMI", "SALARY", "BIRTHDAY"]
        self.assertListEqual(csv._fieldnames, items)

    def test_03(self):
        items = ["EMPID", "GENDER", "AGE", "SALES", "BMI", "SALARY", "BIRTHDAY"]
        data_keys = list(map(lambda i: i.name, Data))
        self.assertListEqual(data_keys, items)

    def test_04(self):
        values = [0, 1, 2, 3, 4, 5, 6]
        data_values = list(map(lambda i: i.value, Data))
        self.assertListEqual(data_values, values)

    def test_05(self):
        csv = CSVOperations("staffinfo123.csv")
        self.assertFalse(csv.file_exist())

    def test_06(self):
        self.assertTrue(hasattr(CSVOperations, "read"))

    def test_07(self):
        self.assertTrue(hasattr(CSVOperations, "save"))

    def test_08(self):
        self.assertTrue(callable(getattr(CSVOperations, "read")))

    def test_09(self):
        self.assertTrue(callable(getattr(CSVOperations, "save")))

    def test_10(self):
        vld = DataValidator()
        self.assertTrue(len(vld.validators) == 7)

    def test_11(self):
        csv = CSVOperations("staffinfo.csv")
        self.assertRaises(AttributeError, csv.save, "This is a data list")

    def test_12(self):
        self.assertRegex("heisoverweight$3333", r".*(?P<bmi>normal|overweight|obesity|underweight).*")

    def test_13(self):
        self.assertRegex("her salaryis$333last year", r"\D*(?P<salary>[0-9]{2,3})\D*")

    def test_14(self):
        csv = CSVOperations("staffinfo.csv")
        self.assertTrue(type(csv.read()) == list)

    def test_15(self):
        staff_data = StaffData()
        staff_data.select_source("csv", "staffinfo.csv")
        self.assertIsInstance(staff_data._source, CSVOperations)

    def test_16(self):
        staff_data = StaffData()
        staff_data.select_source("source")
        self.assertIsNone(staff_data._source)

    def test_17(self):
        staff_data = StaffData()
        self.assertRaises(OSError, staff_data.save_data)

    def test_18(self):
        staff_data = StaffData()
        staff_data.data = [{
            "EMPID": "T123",
            "AGE": 33,
            "GENDER": "M",
            "SALES": 200,
            "BMI": "Normal",
            "SALARY": 200,
            "BIRTHDAY": "31-12-1985"}]
        new_data = ["T123", 26, "F", 150, "Normal", 100, "01-01-1992"]
        self.assertTrue(staff_data.data_exist(new_data))


if __name__ == "__main__":
    main()
