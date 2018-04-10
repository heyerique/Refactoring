from enum import Enum, unique


@unique
class Data(Enum):
    """
    Enum for data
    :Author: Zhiming Liu
    """
    EMPID = 0
    GENDER = 1
    AGE = 2
    SALES = 3
    BMI = 4
    SALARY = 5
    BIRTHDAY = 6
