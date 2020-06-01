import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, 1)
        print("ab同学今年19岁")


if __name__ == '__main__':
    unittest.main()
