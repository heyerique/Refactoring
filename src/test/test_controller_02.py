import unittest
import unittest.mock
from io import StringIO
from os import path, remove, getcwd, chdir
from controller import Controller


class TestController02(unittest.TestCase):
    def setUp(self):
        self.ctl = Controller()

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def assert_import_stdout(self, cmdline, expected_output, mock_stdout):
        self.ctl.do_import(cmdline)
        self.assertIn(expected_output, mock_stdout.getvalue())

    def test_do_import_01(self):
        cmdline = 'invalid command'
        result = 'Invalid command.'
        self.assert_import_stdout(cmdline, result)

    def test_do_import_02(self):
        cmdline = '-csv testingdata_notexist.csv'
        result = 'No such file or directory'
        self.assert_import_stdout(cmdline, result)

    def test_do_import_03(self):
        cmdline = '-csv testingdata.csv'
        result = 'IMPORTING RESULT:'
        self.assert_import_stdout(cmdline, result)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_do_import_04(self, mock_stdout):
        chdir(getcwd())  # pragma: no cover
        pk_path = 'test_files/testingdata.pk'
        if path.exists(pk_path):  # pragma: no cover
            remove(pk_path)  # pragma: no cover

        self.ctl.do_select('-csv')  # pragma: no cover
        self.ctl.do_export('-pk ' + pk_path)  # pragma: no cover

        cmdline = '-pk ' + pk_path
        result = 'IMPORTING RESULT:'
        self.assert_import_stdout(cmdline, result)

    def test_do_import_05(self):
        cmdline = '-pk fakefile.pk'
        result = 'The path or the file doesn\'t exist'
        self.assert_import_stdout(cmdline, result)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_do_import_06(self, mock_stdout):
        self.ctl.do_select('-csv testingdata.csv')

        cmdline = '-csv testingdata.csv'
        result = 'IMPORTING RESULT:'
        self.assert_import_stdout(cmdline, result)


if __name__ == '__main__':  # pragma: no cover
    unittest.main(verbosity=2)  # pragma: no cover
