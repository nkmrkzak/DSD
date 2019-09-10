import unittest
import doctest
import src_ex01 as src


class TestEx01(unittest.TestCase):
        def test_thing(self):
                """
                Thingクラスとexampleオブジェクトは異なる値が表示される。
                """
                expected = "<class 'src_ex01.Thing'>"
                actual = str(src.Thing)
                self.assertEqual(expected, actual)
                
                import re
                expected_example_reg = re.compile("<src_ex01.Thing object at .*>")
                example = src.Thing()
                self.assertTrue(expected_example_reg.match(str(example)))

if __name__ == '__main__':
    unittest.main()