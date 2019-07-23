import unittest
import doctest
import src_ex02 as src

class TestEx02(unittest.TestCase):
    ''' ex0302'''
    def test_get_three_years_old(self):
        expected = 2003
        years_list = src.get_years_list(2000)
        self.assertEqual(expected, src.get_three_years_old(years_list))
    
    def test_get_three_years_old_not_list(self):
        expected = 'a'
        actual = src.get_three_years_old('Invalid arg')
        self.assertEqual(expected, actual)
    
    def test_get_three_years_old_none(self):
        with self.assertRaises(TypeError, msg='aaaaa'):
            src.get_three_years_old(None)

def load_tests(loader, tests, ignore):
        tests.addTests(doctest.DocTestSuite(src))
        return tests

if __name__ == '__main__':
    unittest.main()