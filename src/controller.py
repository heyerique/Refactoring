from cmd import Cmd
from csv import Error as CSVError
from data_validator import DataValidator
from view_console import ViewConsole as View
from staff_data import StaffData
from data import Data
from csv_operations import CSVOperations
from pickle_operations import PickleOperations


class Controller(Cmd):
    def __init__(self):
        Cmd.__init__(self)

        # The command line indicator
        self.prompt = ">>> "

        # Welcome information
        self.intro = "Welcome to Staff Information System\n" \
                     "Enter a keyword to start. For help, enter \"help\"."

        # Object of DataValidator, for validating data
        self._vld = DataValidator()

        # Instance of StaffData
        self._std = StaffData()

    def do_select(self, line):
        """
        Select a data source
        :param line: <String> Source name
        :return: None
        :Author: Zhiming Liu
        """
        # Available data sources
        options = "-csv", "-db"
        args = list(arg.lower() for arg in str(line).split())

        try:
            # Check if the input data source is available
            if args[0] not in options:
                raise Exception("The data resource is not available.")
            else:
                # Code for initialise CSV data source
                if args[0] == "-csv":
                    try:
                        if len(args) == 1:
                            self._std.select_source(args[0][1:],
                                                    "staffinfo.csv")
                            View.warning("No CSV file path specified. "
                                         "A default file \"staffinfo.csv\" "
                                         "will be used.")
                        elif len(args) == 2:
                            self._std.select_source(args[0][1:], args[1])
                        elif len(args) == 3:
                            if args[1] == "-a":
                                self._std.select_source(args[0][1:],
                                                        args[2],
                                                        True)
                            else:
                                raise Exception('Invalid command.')
                        else:
                            raise Exception('Invalid command.')
                    except (CSVError, OSError) as e:
                        View.error(e)
                    except Exception as e:
                        View.error(e)
                    else:
                        View.success("Data source CSV is selected.")

                # Code for initialise database source
                elif args[0] == "-db":
                    self._std.select_source(args[0][1:])

        # Catch and display error message
        except Exception as e:
            View.error(e)
            View.help_select()

    def do_add(self, line):
        """
        Add a new entry of data
        :param line: (String) [EMPID] [Age] [Gender] [Sales]
                    [BMI] [Salary] [Birthday]
        :return: None
        :Author: Zhiming Liu
        """
        # Split the input argument to obtain the data
        raw_data = list(arg.lower() for arg in str(line).split())

        try:
            # Check if input data has 7 data fields
            if not len(raw_data) == len(Data):
                raise AttributeError("Please input correct data.")
            else:
                # Check and wash data by check_all() of DataValidator
                result = self._vld.check_all(raw_data)
                # Check if there is any None which stands for invalid input
                if None in result:
                    key = 0
                    # build a list of name list
                    items = list(map(lambda i: i.name, Data))
                    e_str = ""
                    while key < len(result):
                        if result[key] is None:
                            # Left alignment
                            e_str += "{:<10}".format(items[key])
                        key += 1
                    raise ValueError("The following field(s) "
                                     "is invalid:\n%s" % e_str)
                else:
                    self._std.add_data(result)
        except (AttributeError, ValueError) as e:
            View.error(str(e) + "\n")
            View.help_add()
        except CSVError as e:
            View.error(e)
        except Exception as e:
            View.error(e)
        else:
            View.success("Add data")

    def do_import(self, line):
        """
        Import command
        :param line: (String) [-csv|-pk] [file path]
        :return: None
        :Author: Zhiming Liu
        """
        args = list(arg.lower() for arg in str(line).split())

        # CSV
        if args[0] == "-csv" and len(args) > 1:
            try:
                csv = CSVOperations(args[1])
                import_data = csv.read()
                View.display("IMPORTING RESULT:")
                View.import_result_header(True)
                for d in import_data:
                    View.import_result_row(self.import_row(d), True)
            except Exception as e:
                View.error(e)
        # Pickle
        elif args[0] == "-pk" and len(args) > 1:
            try:
                pk = PickleOperations()
                import_data = list(pk.pickle_import(args[1]))
                View.display("IMPORTING RESULT:")
                View.import_result_header(True)
                for d in import_data:
                    View.import_result_row(self.import_row(d), True)
            except Exception as e:
                View.error(e)
            else:
                View.success("Data has been loaded from %s" % args[1])
        else:
            View.info("Invalid command.")
            View.help_import()

    def import_row(self, raw_data):
        """
        Add a new data from imported files
        :param raw_data: Dict
        :return: Dict
        :Author: Zhiming Liu
        """
        result = list(raw_data.values())
        try:
            washed = self._vld.check_all(list(raw_data.values()))
            if None in washed:
                result.append("Fail")
            else:
                self._std.add_data(washed)
                result.append("Pass")
        except ValueError:
            result.append("Fail")
        except AttributeError:
            result.append("Fail")
        except Exception:
            result.append("Fail")
        finally:
            return result

    def do_export(self, line):
        """
        Export command
        :param line: (String) [-pk] [file path]
        :return: None
        :Author: Zhiming Liu
        """
        args = list(arg.lower() for arg in str(line).split())
        if args[0] == "-pk" and len(args) > 1:
            try:
                pk = PickleOperations()
                pk.pickle_dump(args[1], self._std.get_all_data())
            except Exception as e:
                View.error(e)
                View.help_export()
            else:
                View.success("Data has been saved to %s" % args[1])
        else:
            View.info("Invalid command")
            View.help_export()

    def do_save(self, arg):
        """
        Save data to specified data source
        :param arg: arg
        :return: None
        :Author: Zhiming Liu
        """
        # If no data source selected, prompt user to do so.
        try:
            self._std.save_data()
        except ValueError as e:
            View.info(e)
        except (OSError, AttributeError) as e:
            View.error(e)
        except Exception as e:
            View.error(e)
        else:
            View.success("Data is saved")

    def do_show(self, line):
        """
        Show command
        :param line: (String) [-t|-p|-b] [object]
        :return: None
        :Author: Zhiming Liu
        """
        # Get all instructions
        args = list(arg.lower() for arg in str(line).split())

        # Those commands are required single arguments
        # single_commands = ["-a"]
        # Those commands are required two arguments
        plot_commands = ["-p", "-b"]

        # Show data table
        if args[0] == "-t":
            if len(self._std.data) == 0 and len(self._std.new_data) == 0:
                View.info("No data to display.")
            if not len(self._std.data) == 0:
                View.display("ORIGINAL DATA:")
                View.display_data(self._std.data, ind=True)
            if not len(self._std.new_data) == 0:
                View.display("\nNEW DATA:")
                View.display_data(self._std.new_data, ind=True)
                View.display("\n(Input command \"save\" to save the new data)")

        elif args[0] in plot_commands:
            try:
                if len(args) == 1:
                    raise IndexError("Incomplete command line.")

                if args[0] == "-p":
                    self.show_pie(args[1])
                if args[0] == "-b":
                    self.show_bar(args[1])

            except IndexError as e:
                View.error(str(e) + "\n")
                View.help_show()
        else:
            View.info("Invalid command line.\n")
            View.help_show()

    def show_pie(self, line):
        """
        Draw pie chart
        :param line: String
        :return: None
        :Author: Zhiming Liu
        """
        # Draw Pies
        try:
            if self._std.get_gender().total_count == 0 \
                    or len(self._std.get_bmi()) == 0:
                raise ValueError("No data to display.")
            # Draw gender
            if line.upper() == Data.GENDER.name:
                View.plot_pie(self._std.get_gender().formatted_data,
                              "Gender Distribution",
                              "People")
            # Draw BMI
            if line.upper() == Data.BMI.name:
                View.plot_pie(self._std.get_bmi(),
                              "Body Mass Index (BMI)",
                              "People")
        except ValueError as e:
            View.info(e)
        except Exception as e:
            View.error(e)

    def show_bar(self, line):
        """
        Draw bar chart
        :param line: String
        :return: None
        :Author: Zhiming Liu
        """
        # Draw Bars
        try:
            if self._std.get_gender().total_count == 0 \
                    or len(self._std.get_bmi()) == 0:
                raise ValueError("No data to display.")
            # Draw gender
            if line.upper() == Data.GENDER.name:
                View.plot_bar(self._std.get_gender().formatted_data,
                              "Gender Distribution",
                              "numer of people")
            # Draw BMI
            if line.upper() == Data.BMI.name:
                View.plot_bar(self._std.get_bmi(),
                              "Body Mass Index (BMI)",
                              "number of people")
        except ValueError as e:
            View.info(e)
        except Exception as e:
            View.error(e)

    @staticmethod
    def help_show():
        View.display("This command is used for displaying all data that "
                     "is existed in the system.\n")
        View.help_show()

    @staticmethod
    def help_add():
        View.display("This command adds a new staff data to the system.\n")
        View.help_add()

    @staticmethod
    def help_save():
        View.display("This command is used for saving all newly added data "
                     "to the selected data source.\n")
        View.help_save()

    @staticmethod
    def help_select():
        View.display("Select a source of data for reading "
                     "and saving staff information.\n")
        View.help_select()

    @staticmethod
    def help_quit():
        View.display("This command is used for "
                     "quitting the command line mode\n")
        View.help_quit()

    @staticmethod
    def help_import():
        View.display("Import data from a file "
                     "that is specified in the command line.\n")
        View.help_import()

    @staticmethod
    def help_export():
        View.display("Export data to a local file "
                     "that is specified in the command line.\n")
        View.help_export()

    def do_quit(self, line):
        arg = str(line).lower()
        if not arg == "-f" and not len(self._std.new_data) == 0:
            View.warning("The new data hasn't been saved. "
                         "Enter \"quit -f\" to quit without saving.")
        else:
            View.display("Thanks for using. Bye!")
            return True


if __name__ == "__main__":
    ctl = Controller()
    ctl.cmdloop()
