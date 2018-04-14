from pickle import dump, load
from os import path, makedirs, getcwd, chdir


class PickleOperations:
    """
    This is class for dump pickled file to a local file,
    and load data from a local file
    :Author: Zhiming Liu
    """
    def pickle_dump(self, filepath, data):
        """
        Write pickled data to a local file
        :param filepath: String
        :param data: list
        :return: None
        """
        self.check_path(filepath)

        chdir(getcwd())

        with open(filepath, "wb") as pfile:
            dump(data, pfile)

    @staticmethod
    def pickle_import(filepath):
        """
        Read pickled data from a local file
        :param filepath: String
        :return: None
        """
        chdir(getcwd())
        if not path.exists(filepath):
            raise OSError("The path or the file doesn't exist")

        with open(filepath, "rb") as pfile:
            return load(pfile)

    @staticmethod
    def check_path(filepath):
        """
        Check if the given path path exists. Create one if it doesn't exist.
        :param filepath: String
        :return: None
        """
        filedir, filename = path.split(filepath)

        chdir(getcwd())

        if not filedir == "" and not path.exists(filedir):
            makedirs(filedir)

        if not path.exists(filepath):
            with open(filepath, "w+"):
                pass
        else:
            raise OSError("Can't create the file. The file already exists.")
