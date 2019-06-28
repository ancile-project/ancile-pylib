import unittest
from ancile.wrappers import ancile_function

class TestAncileFunction(unittest.TestCase):

    def test_noargs(self):

        @ancile_function
        def my_func():
            x = 5
            y = x + 1
            return y

        @ancile_function
        def my_second_func():
            my_second_func_var = 5
            return my_second_func_var
        
        self.assertEqual(
            my_func(),
            '''x = 5
y = x + 1
return y
'''
        )

        self.assertEqual(
            my_second_func(),
            '''my_second_func_var = 5
return my_second_func_var
'''
        )
    
    def test_onearg(self):

        do_something = lambda x: x

        @ancile_function
        def my_func(x):
            y = do_something(x)
            return y

        self.assertEqual(
            my_func(5),
            "y = do_something(5)\nreturn y\n"
        )

        self.assertEqual(
            my_func("user"),
            "y = do_something('user')\nreturn y\n"
        )

        self.assertEqual(
            my_func([1,2]),
            "y = do_something([1, 2])\nreturn y\n"
        )
