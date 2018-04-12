import unittest
import unittest.mock
from io import StringIO
from os import path, remove
from controller import Controller

class TestController01(unittest.TestCase):
    def setUp(self):
        self.ctl = Controller()

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def assert_select_stdout(self, cmdline, expected_output, mock_stdout):
        self.ctl.do_select(cmdline)
        self.assertIn(expected_output, mock_stdout.getvalue())

    def test_do_select_01(self):
        cmdline = '-csv'
        result = 'No CSV file path specified. A default file \"staffinfo.csv\" will be used.'
        self.assert_select_stdout(cmdline, result)

    def test_do_select_02(self):
        cmdline = 'invalid command'
        result = 'The data resource is not available.'
        self.assert_select_stdout(cmdline, result)

    def test_do_select_03(self):
        cmdline = '-csv testingdata.csv'
        result = 'Data source CSV is selected.'
        self.assert_select_stdout(cmdline, result)

    def test_do_select_04(self):
        cmdline = '-csv -a staffinfo.csv'
        result = 'Can\'t create the file. The file already exists.'
        self.assert_select_stdout(cmdline, result)

    def test_do_select_05(self):
        cmdline = '-db'
        result = ''
        self.assert_select_stdout(cmdline,result)

    def test_do_select_06(self):
        cmdline = '-csv -invalid -command'
        result = 'Invalid command.'
        self.assert_select_stdout(cmdline, result)

    def test_do_select_07(self):
        cmdline = '-csv -this -is -an -invalid -command'
        result = 'Invalid command.'
        self.assert_select_stdout(cmdline, result)


if __name__ == '__main__': # pragma: no cover
    unittest.main(verbosity=2) # pragma: no cover
