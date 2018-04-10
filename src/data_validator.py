import re
from data import Data
from time import strptime


class DataValidator:

    def __init__(self):
        # A function list if validators
        self.validators = (
            self.check_empid, self.check_gender, self.check_age,
            self.check_sales, self.check_bmi, self.check_salary,
            self.check_birthday
        )

    @staticmethod
    def check_empid(data):
        """
        Check if the input empID is valid.
        :return: Formatted empid if the input one is valid, otherwise, return None
        Author: Vaishali Patel
        """
        # Convert the input data to string
        empid = str(data)

        # Regular expression checks if there are combination of [A-Z][0-9]{3} e.r E101
        # :P<empid> Assign to the group with the keyword 'empid'
        pattern = r"^(?P<empid>[A-Z][0-9]{3})$"
        match_obj = re.search(pattern, empid, re.I)
        if match_obj:
            # Get the matched word
            empid = match_obj.group("empid")
            # Convert the first letter to Uppercase and lowercase for rest of them

            return empid.upper()
        # Return None if no match found
        return None

    @staticmethod
    def check_gender(data):
        """
        Check validation of gender
        :param gender: <String>
        :return: washed data
        :Author: Zhiming Liu
        """
        gender = str(data)
        pattern_01 = r"^(?P<gender>F\w*|M\w*)$"
        pattern_02 = r"^(?P<gender>girl|boy)$"
        match_01 = re.match(pattern_01, gender, re.I)
        result = None
        if match_01:
            gender = match_01.group("gender").upper()
            result = gender[0]
        else:
            match_02 = re.match(pattern_02, gender, re.I)
            if match_02:
                gender = match_02.group("gender").upper()
                result = "F" if gender == "GIRL" else "M"
        return result

    @staticmethod
    def check_age(data):
        """
        Check validation of age
        :param age: <String>
        :return: washed data
        :Author: Zhiming Liu
        """
        age = str(data)
        pattern = r"^(?P<age>[0-9]{1,2})$"
        match_obj = re.match(pattern, age)
        if match_obj:
            # Convert the match to integer and return
            return "{0:02}".format(int(match_obj.group("age")))
        # Return None if no match found
        return None

    @staticmethod
    def check_sales(data):
        """
        Check if the input sales is valid.
        :return: Formatted sales if the input one is valid, otherwise, return None
        :Author: Zhiming Liu
        """
        # Regular expression checks if there are consecutive 3 numbers
        # :P<salary> Assign to the group with the keyword 'salary'
        sales = str(data)
        pattern = r"^(?P<sales>[0-9]{1,3})$"
        match_obj = re.search(pattern, sales)
        if match_obj:
            # Convert the match to integer and return
            return "{0:03}".format(int(match_obj.group("sales")))
        # Return None if no match found
        return None

    @staticmethod
    def check_bmi(data):
        """
        Check if the input BMI is valid.
        :return: Formatted BMI if the input one is valid, otherwise, return None
        :Author: Zhiming Liu
        """
        # Convert the input data to string
        bmi = str(data)

        # Regular expression checks if any of the specified keywords exists
        # :P<bmi> Assign to the group with the keyword 'bmi'
        pattern = r".*(?P<bmi>normal|overweight|obesity|underweight).*"
        match_obj = re.search(pattern, bmi, re.I)
        if match_obj:
            # Get the matched word
            bmi = match_obj.group("bmi")
            # Convert the first letter to uppercase and lowercase for rest of them
            bmi = " ".join(text[0].upper() + text[1:] for text in bmi.split())  # Capitalise the first letter
            return bmi
        # Return None if no match found
        return None

    @staticmethod
    def check_salary(data):
        """
        Check if the input salary is valid.
        :return: Formatted salary if the input one is valid, otherwise, return None
        :Author: Zhiming Liu
        """
        # Regular expression checks if there are consecutive 3 numbers
        # :P<salary> Assign to the group with the keyword 'salary'
        salary = str(data)
        pattern = r"^(?P<salary>[0-9]{2,3})$"
        match_obj = re.search(pattern, salary)
        if match_obj:
            # Convert the match to integer and return
            return "{0:03}".format(int(match_obj.group("salary")))
        # Return None if no match found
        return None

    @staticmethod
    def check_birthday(data):
        """
        Check validation of birthday
        :param birthday: <String>
        :return: washed data
        :Author: Zhiming Liu
        """
        birthday = str(data)
        pattern = r"^([0-9]{1,2})[-/\.]([0-9]{1,2})[-/\.]([0-9]{2}|[0-9]{4})$"
        match = re.match(pattern, birthday)
        if match:
            date = "-".join(match.groups())
            struct = strptime(date, "%d-%m-%Y")
            return "{0:02}-{1:02}-{2:04}".format(struct.tm_mday, struct.tm_mon, struct.tm_year)
        else:
            return None

    def check_all(self, all_data: list):
        """
        Check validation of the all data. Throw ValueError Exceptions.
        :param all_data: a data list
        :return: washed data in dictionary
        :Author: Zhiming Liu
        """
        # Save the washed data temporarily
        result = []

        # If the number of the data is not correct, return an empty result
        if not len(all_data) == len(Data):
            return result

        # Check and wash data
        key = 0
        while key < len(all_data):
            # Get the validation function by the order of the data
            v = self.validators[key]
            # Append to the result
            result.append(v(all_data[key]))
            key += 1

        return result


# print(DataValidator.check_bmi("jbjndsoidiri88888normaljdjdjd"))
# v = DataValidator()
# print(DataValidator.check_birthday("31-02-1990"))
