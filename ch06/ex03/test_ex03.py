import unittest
import doctest
import src_ex03 as src


class TestEx03(unittest.TestCase):
        def test_thing3(self):
            expected = 'xyz'
            actual = src.Thing3().letters
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
