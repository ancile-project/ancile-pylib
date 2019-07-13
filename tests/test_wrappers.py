import unittest
from ancile.wrappers import ancile_program

class TestAncileProgram(unittest.TestCase):

    def test_noargs(self):

        @ancile_program
        def my_func():
            x = 5
            y = x + 1
            return y

        @ancile_program
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

        @ancile_program
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

    def test_twoargs(self):

        do_something = lambda x: x

        @ancile_program
        def my_func(x, z):
            y = do_something(x, z)
            return y

        self.assertEqual(
            my_func(5, 4),
            "y = do_something(5, 4)\nreturn y\n"
        )

        self.assertEqual(
            my_func("user", "sam"),
            "y = do_something('user', 'sam')\nreturn y\n"
        )

        self.assertEqual(
            my_func([1,2], [3,4]),
            "y = do_something([1, 2], [3, 4])\nreturn y\n"
        )
    
    def test_with_underscore_param(self):

        @ancile_program
        def my_func(_param_name, _user="Sam"):
            _param_name = type(_user)
        

        self.assertEqual(
            my_func("param"),
            "param = type(Sam)\n"
        )
    
    def test_with_gap_beggining(self):
        @ancile_program
        def my_func():



            return
        
        @ancile_program
        def another_func(_param, name, year=0, _type="test"):


            _param = type(name)

            return _param, year, _type
        
        self.assertEqual(
            my_func(),
            "return\n"
        )

        self.assertEqual(
            another_func("first", "second", 43),
            "first = type('second')\nreturn first, 43, test\n"
        )
