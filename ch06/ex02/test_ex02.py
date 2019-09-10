import unittest
import doctest
import src_ex02 as src


class TestEx02(unittest.TestCase):
        def test_thing2(self):
            expected = 'abc'
            actual = src.Thing2.letters
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
