import csv
from os import path, makedirs
from idata_access import IDataAccess
from data import Data


class CSVOperations(IDataAccess):
    """
    This is class for reading from a specified CSV file and writing new data to it
    :Author: Zhiming Liu
    """
    # CSV file path
    __path = None
    __file_path = None
    __file_name = None

    # The header of data field in the CSV file. Also for data dictionaries
    _fieldnames = None

    def __init__(self, file_path, create=False):

        self.__path = file_path
        paths = str(file_path).split("/")
        if len(paths) > 1:
            self.__file_path = "/".join(paths[0:-1])
        self.__file_name = paths[-1]

        # Initialise fieldnames
        self._fieldnames = list(map(lambda i: i.name, Data))
        # Create the file if it doesn't exist
        # chdir("./")
        if create:
            self.create_file()

    def create_file(self):
        """
        Create the CSV file at specified path
        :return: None
        """
        if self.__file_path is not None and not path.exists(self.__file_path):
            makedirs(self.__file_path)
        # chdir(self.__file_path)
        if not self.file_exist():
            with open(self.__path, "w+") as f:
                writer = csv.writer(f, lineterminator="\n")
                writer.writerow(list(d.name for d in Data))
        else:
            raise OSError("Can't create the file. The file already exists.")

    def read(self):
        """
        This function return content of the CSV file
        :return: None
        """
        # Try to open the file for read. newline to avoid different newline signs
        with open(self.__path, newline="") as f:
            # Try to read data with given fieldnames
            reader = csv.DictReader(f, fieldnames=self._fieldnames)
            # Save data in an array, but ignore the first line
            data = list(dict(row) for row in reader)[1:]

        return data

    def file_exist(self):
        """
        Check if the giving file/path exists
        :return:
        """
        return path.exists(self.__path)

    def save(self, data: list):
        """
        This function saves new data to the CSV file
        """
        # If the data type of data is not List, raise an exception
        # Those exceptions need to be caught when the function is called
        if not type(data) == list:
            raise AttributeError("Data should be a list.")
        # Raise an exception if the file/path doesn't exist
        # Those exceptions need to be caught when the function is called
        elif not self.file_exist():
            raise OSError("The CSV file does not exist.")
        else:
            # Open the file to write
            with open(self.__path, "a") as f:
                # Write all temporary data list to the file
                writer = csv.writer(f, lineterminator="\n")
                for row in data:
                    writer.writerow(row.values())


# op = CSVOperations('files/data/staffinfo3.csv', True)
# # print(op.read())
# new_data_01 = [{"empid": "Y413", "gender": "M", "age": 41, "sales": 200,
# "bmi": "Obesity", "salary": 450, "birthday": "01-09-1977"}, {"empid": "Y414", "gender": "F", "age": 33, "sales": 200,
# "bmi": "Obesity", "salary": 450, "birthday": "04-10-1985"}]
# op.save(new_data_01)
