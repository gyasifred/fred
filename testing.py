import unittest
import fred


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = fred.do_stuff(test_param)
        self.assertEqual(result, 50)


    def test_do_stuff2(self):
        test_param = 'gyasi'
        result = fred.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)


    def test_do_stuff3(self):
    	test_param = None
    	result = fred.do_stuff(test_param)
    	self.assertEqual(result, 'please enter number')


if __name__ == '__main__':
	unittest.main()
