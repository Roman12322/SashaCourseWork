import unittest

from SashaCourseWork.project.func import function


class funtest(unittest.TestCase):
    def setUp(self):
        pass

    def test_funtest1(self):
        result = function('123123', '123122')
        self.assertEqual(1.0, result)

    def test_funtest2(self):
        result = function('qwer', 'qqqq')
        self.assertEqual(3.0, result)

    def test_funtest3(self):
        result = function('А', 'Russia')
        self.assertEqual(6.0, result)

    def test_funtest4(self):
        result = function('tusur', 'msu')
        self.assertEqual(3.0, result)

    def test_funtest5(self):
        result = function('', 'profcom')
        self.assertEqual(7, result)

    def test_funtest6(self):
        result = function('lolipop', '')
        self.assertEqual(7, result)

    def test_funtest7(self):
        result = function('', '')
        self.assertEqual(0, result)