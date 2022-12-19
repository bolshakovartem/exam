import unittest
import app


class MyTestCase(unittest.TestCase):

    a0 = 2
    d = 2
    n = 6
    def setUp(self):
        self.app = app.app.test_client()

    def test_arifm_prog(self):

        k = app.arifm_prog(MyTestCase.a0, MyTestCase.d, MyTestCase.n)
        res = 12
        self.assertEqual(k, res)

    def test_sum_arifm_progr(self):

        k = app.sum_arifm_progr(MyTestCase.a0, MyTestCase.d, MyTestCase.n)
        res = 42
        self.assertEqual(k, res)



if __name__ == '__main__':
    unittest.main()
