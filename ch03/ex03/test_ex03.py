import unittest
import doctest
import src_ex03 as src

class TestEx03(unittest.TestCase):
    ''' ex0303'''
    def test_get_latest_years_old(self):
        expected = 2004
        years_list = src.get_years_list(2000)
        self.assertEqual(expected, src.get_latest_years_old(years_list))

def load_tests(loader, tests, ignore):
        tests.addTests(doctest.DocTestSuite(src))
        return tests

if __name__ == '__main__':
    unittest.main()