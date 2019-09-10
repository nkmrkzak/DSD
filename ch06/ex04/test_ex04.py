import unittest
import doctest
import src_ex04 as src


class TestEx4(unittest.TestCase):
    def test_element(self):
        expected = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
        elem = src.Element(name='Hydrogen', symbol='H', number=1)
        self.assertEqual(expected['name'], elem.name)
        self.assertEqual(expected['symbol'], elem.symbol)
        self.assertEqual(expected['number'], elem.number)

if __name__ == '__main__':
    unittest.main()
