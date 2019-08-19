from unittest import TestCase, main
from zoo import coretime
from workException import OverworkedException


class TestFoo(TestCase):

    def test_coretime(self):
        self.assertEqual(coretime(9, 5), 'Open 9-5 daily')
        self.assertEqual(coretime(9, 17), 'Open 9-17 daily')

    def test_coretime_valueException(self):
        with self.assertRaises(ValueError):
            coretime(0, 5)
        with self.assertRaises(ValueError):
            coretime(25, 5)
        with self.assertRaises(ValueError):
            coretime(9, 0)
        with self.assertRaises(ValueError):
            coretime(9, 25)

    def test_coretime_overworkException(self):
        with self.assertRaises(OverworkedException):
            coretime(5, 21)
        with self.assertRaises(OverworkedException):
            coretime(9, 20, 10)


if __name__ == "__main__":
    main()
