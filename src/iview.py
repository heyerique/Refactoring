from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    """
    Interface for output implementation
    """

    @staticmethod
    @abstractmethod
    def display(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def error(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def success(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def warning(text):
        """
        Output Warning
        :param text: A text string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def info(text):
        """
        Output Info
        :param text: A text string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def display_data(data, ind=False):
        """
        Output data
        :param data: (list)
        :param ind: (Boolean)
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def import_result_header(ind=False):
        """
        display the header of the table
        :param ind: (Boolean)
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def import_result_row(row, ind=False):
        """
        display a row of the table
        :param row: (list)
        :param ind: (Boolean)
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def plot_pie(data, title=""):
        """
        Plot a pie chart for gender, BMI
        :param data: data dictionary
        :param title: string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def plot_bar(data, title=""):
        """
        Plot a vertical bar chart for sales, salary, age...
        :param data: dictionary,
        :param title: string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def plot_barh(data, title=""):
        """
        Plot a horizontal bar chart for sales, salary, age...
        :param data: dictionary,
        :param title: string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def help_show():
        pass

    @staticmethod
    @abstractmethod
    def help_select():
        pass

    @staticmethod
    @abstractmethod
    def help_add():
        pass

    @staticmethod
    @abstractmethod
    def help_import():
        pass

    @staticmethod
    @abstractmethod
    def help_export():
        pass

    @staticmethod
    @abstractmethod
    def help_save():
        pass

    @staticmethod
    @abstractmethod
    def help_quit():
        pass
