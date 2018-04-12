from test import *
import unittest


def suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(TestController01))
    the_suite.addTest(unittest.makeSuite(TestController02))
    the_suite.addTest(unittest.makeSuite(TestController03))
    the_suite.addTest(unittest.makeSuite(TestDataValidator))
    # the_suite.addTest(unittest.makeSuite(TestStaffData))
    return the_suite

if __name__ == '__main__': # pragma: no cover
    runner = unittest.TextTestRunner(verbosity=2) # pragma: no cover
    test_suite = suite() # pragma: no cover
    runner.run(test_suite) # pragma: no cover
