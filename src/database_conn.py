
import sqlite3
from idata_access import IDataAccess
from data import Data

class Database(IDataAccess):
    # Written By Vaishali
    #
    # This is the MySQL Database connection class
    #
    #
    def __init__(self):
        # Written By Vaishali
        # The first method __init__() is a special method,
        # which is called class constructor or initialization method
        # creates to null veriable
        #
        self.conn = None
        self.cursor = None
        self.create_db_connection("staffinfo")

    def create_db_connection(self, database_name):
        # Written by Vaishali
        #
        # This method to creates the connection with the database.
        #
        # Tries to handles the error if
        # no connection can be made. make the connection otherwise
        #
        # when database connect successfully then the conn atribute is given to
        # the connection object
        # and the cursor the cursor object.
        #
        # It then calls the make_tables method.
        #
        try:
            self.conn = sqlite3.connect(database_name)
            self.cursor = self.conn.cursor()
            self.make_tables()     # call make_table method here
        except (ConnectionError, TypeError) as err:   # If type error
            print(err)             # Raised when an operation or function is attempted
        except Exception as e:                      # that is invalid for the specified data type.
           print(e)

    def make_tables(self):
        # Written By Vaishali
        #
        # This is called from the create_db_connection method.
        # Create the employee table within the database.
        #
        # This only happens if the table doesnt exist.
        #
        #
        #    drop_table if exists

        make_table = """CREATE TABLE IF NOT EXISTS EMPLOYEE ({0} VARCHAR(6),
                     {1} CHAR, {2} INTERGER, {3} INTERGER, 
                     {4} VARCHAR(15), {5} INTERGER, {6} DATE);"""
        make_table = self.format_col(make_table)
        self.cursor.execute (make_table)
        self.conn.commit ()

    def format_col(self, sql):
        return sql.format(Data.EMPID.name,
                         Data.GENDER.name,
                         Data.AGE.name,
                         Data.SALES.name,
                         Data.BMI.name,
                         Data.SALARY.name,
                         Data.BIRTHDAY.name)

    def insert_employee_data(self, data_row):
        # Written By Vaishali
        #
        #
        #
        # employee_data = [("A001","F","23","456","Normal","14","30/05/1994"),
        #                  ("A221","F","49","458","Normal","244","30/05/1994"),
        #                  ("C342","M","50","676","Overweight","300","1/12/1977"),
        #                  ("D123","F","55","123","Obesity","600","15/01/1997")]

        try:
            insert_string_1 = "INSERT INTO employee ({0} ,{1}, {2}, {3}, {4}, {5}, {6}) "
            insert_string_2 = self.format_col(insert_string_1)
            insert_string_2 += """VALUES ("{0}", "{1}", "{2}", "{3}", "{4}",
              "{5}", "{6}");"""
            try:
                insert_command = insert_string_2.format(data_row[Data.EMPID.name],
                                                        data_row[Data.GENDER.name],
                                                        data_row[Data.AGE.name],
                                                        data_row[Data.SALES.name],
                                                        data_row[Data.BMI.name],
                                                        data_row[Data.SALARY.name],
                                                        data_row[Data.BIRTHDAY.name])
                self.cursor.execute(insert_command)
                self.conn.commit()
            except IndexError as err:
                print(err)
                return False

        except AttributeError as err:
            print(err)
            return False
        except UnboundLocalError as err:
            print(err)
            return False
        except TypeError as err:
            print(err)
            return False
        return True

    def save(self, data):
        for d in data:
            self.insert_employee_data(d)

    def read(self):
        # Written By Vaishali
        #
        # This function retrieve all the employee data from the employee table
        # in array format and leter in the another function
        # the data will be set to the specific format

        data_arr = []    # Retrieve employee data in to data_arr "array" format
        try:
            self.cursor.execute("Select * from employee")
            data = self.cursor.fetchall()
            for r in data:
                data_arr.append({d.name : r[d.value] for d in Data})

            return data_arr
        except AttributeError as err:
            print(err)
            return False


# db = Database()
# new_data_01 = [{"EMPID": "Y413", "GENDER": "M", "AGE": 41, "SALES": 200,
# "BMI": "Obesity", "SALARY": 450, "BIRTHDAY": "01-09-1977"}]
# # print(db.save(new_data_01))
# print(db.read())
