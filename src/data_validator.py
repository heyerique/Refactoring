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

    def regx_match(self, pattern, data):
        result = None
        match_obj = re.match(pattern, str(data), re.I)
        if match_obj:
            result = match_obj.group(1)
        return result

    def regx_match_group(self, pattern, data):
        result = None
        match_obj = re.match(pattern, str(data), re.I)
        if match_obj:
            result = match_obj.groups()
        return result

    def check_empid(self, data):
        """
        Check if the input empID is valid.
        :return: Formatted empid if the input one is valid,
        otherwise, return None
        Author: Vaishali Patel
        """
        pattern = r"^(?P<empid>[A-Z][0-9]{3})$"
        result = self.regx_match(pattern, data)
        if result is not None:
            return result.upper()

        return result

    def check_gender(self, data):
        """
        Check validation of gender
        :param gender: <String>
        :return: washed data
        :Author: Zhiming Liu
        """
        pattern_01 = r"^(?P<gender>F|girl|female|miss|ms)$"
        pattern_02 = r"^(?P<gender>M|boy|male|mister|mr)$"

        result = self.regx_match(pattern_01, data)
        if result is not None:
            return 'F'

        result = self.regx_match(pattern_02, data)
        if result is not None:
            return "M"

    def check_age(self, data):
        """
        Check validation of age
        :param age: <String>
        :return: washed data
        :Author: Zhiming Liu
        """
        pattern = r"^(?P<age>[0-9]{1,2})$"
        result = self.regx_match(pattern, data)
        if result is not None:
            return "{0:02}".format(int(result))
        return None

    def check_sales(self, data):
        """
        Check if the input sales is valid.
        :return: Formatted sales if the input one is valid,
        otherwise, return None
        :Author: Zhiming Liu
        """
        pattern = r"^(?P<sales>[0-9]{1,3})$"
        result = self.regx_match(pattern, data)
        if result is not None:
            return "{0:03}".format(int(result))
        return None

    def check_bmi(self, data):
        """
        Check if the input BMI is valid.
        :return: Formatted BMI if the input one is valid,
        otherwise, return None
        :Author: Zhiming Liu
        """
        pattern = r"^(?P<bmi>normal|overweight|obesity|underweight)$"
        result = self.regx_match(pattern, data)
        if result is not None:
            return " ".join(text[0].upper() + text[1:]
                            for text in result.split())
        return None

    def check_salary(self, data):
        """
        Check if the input salary is valid.
        :return: Formatted salary if the input one is valid,
        otherwise, return None
        :Author: Zhiming Liu
        """
        pattern = r"^(?P<salary>[0-9]{2,3})$"
        result = self.regx_match(pattern, data)
        if result is not None:
            return "{0:03}".format(int(result))
        return None

    def check_birthday(self, data):
        """
        Check validation of birthday
        :param birthday: <String>
        :return: washed data
        :Author: Zhiming Liu
        """
        pattern = r"^([0-9]{1,2})[-/\.]([0-9]{1,2})[-/\.]([0-9]{2}|[0-9]{4})$"
        result = self.regx_match_group(pattern, data)
        if result is not None:
            date = strptime("-".join(result), "%d-%m-%Y")
            return "{0:02}-{1:02}-{2:04}"\
                .format(date.tm_mday, date.tm_mon, date.tm_year)
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
