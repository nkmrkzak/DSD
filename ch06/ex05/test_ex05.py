import unittest
import doctest
import src_ex05 as src


class TestEx5(unittest.TestCase):
    def test_element_dict(self):
        expected = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
        elem = src.Element(**expected)
        self.assertEqual(expected['name'], elem.name)
        self.assertEqual(expected['symbol'], elem.symbol)
        self.assertEqual(expected['number'], elem.number)

if __name__ == '__main__':
    unittest.main()
