import unittest
import doctest
import src_ex01 as src


class TestEx01(unittest.TestCase):
    ''' ex0301'''
    def test_get_years_list_born_2000(self):
        expected = [2000, 2001, 2002, 2003, 2004]
        self.assertEqual(expected, src.get_years_list(2000))

    def test_get_years_list_born_2020(self):
        expected = [2020, 2021, 2022, 2023, 2024]
        self.assertEqual(expected, src.get_years_list(2020))

    def test_invalid_arg(self):
        with self.assertRaises(TypeError, msg='must be str, not int'):
            src.get_years_list('invalid arg')


def load_tests(loader, tests, ignore):
        tests.addTests(doctest.DocTestSuite(src))
        return tests

if __name__ == '__main__':
    unittest.main()