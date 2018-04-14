import unittest
import unittest.mock
from io import StringIO
from controller import Controller


class TestController03(unittest.TestCase):
    def setUp(self):
        self.ctl = Controller()

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def assert_show_stdout(self, cmdline, expected_output, mock_stdout):
        self.ctl.do_show(cmdline)
        self.assertIn(expected_output, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_do_show_01(self, mock_stdout):
        self.ctl.do_import('-csv testingdata.csv')
        cmdline = '-p gender'
        result = ''
        self.assert_show_stdout(cmdline, result)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_do_show_02(self, mock_stdout):
        self.ctl.do_import('-csv testingdata.csv')
        cmdline = '-b gender'
        result = ''
        self.assert_show_stdout(cmdline, result)

    def test_do_show_03(self):
        cmdline = '-p gender'
        result = 'No data to display.'
        self.assert_show_stdout(cmdline, result)

    def test_do_show_04(self):
        cmdline = 'invalid command'
        result = 'Invalid command line.'
        self.assert_show_stdout(cmdline, result)

    def test_do_show_05(self):
        cmdline = '-p'
        result = 'Incomplete command line.'
        self.assert_show_stdout(cmdline, result)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_do_show_06(self, mock_stdout):
        self.ctl.do_import('-csv testingdata.csv')
        result = {'Male': 6, 'Female': 4}
        self.assertDictEqual(self.ctl._std.get_gender(), result)

if __name__ == '__main__':  # pragma: no cover
    unittest.main(verbosity=2)  # pragma: no cover
