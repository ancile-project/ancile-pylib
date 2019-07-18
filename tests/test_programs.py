import unittest
from ancile.programs import ancile_program, build_programs


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
            """x = 5
y = x + 1
return y
""",
        )

        self.assertEqual(
            my_second_func(),
            """my_second_func_var = 5
return my_second_func_var
""",
        )

    def test_onearg(self):

        do_something = lambda x: x

        @ancile_program
        def my_func(x):
            y = do_something(x)
            return y

        self.assertEqual(my_func(5), "y = do_something(5)\nreturn y\n")

        self.assertEqual(my_func("user"), "y = do_something('user')\nreturn y\n")

        self.assertEqual(my_func([1, 2]), "y = do_something([1, 2])\nreturn y\n")

    def test_twoargs(self):

        do_something = lambda x: x

        @ancile_program
        def my_func(x, z):
            y = do_something(x, z)
            return y

        self.assertEqual(my_func(5, 4), "y = do_something(5, 4)\nreturn y\n")

        self.assertEqual(
            my_func("user", "sam"), "y = do_something('user', 'sam')\nreturn y\n"
        )

        self.assertEqual(
            my_func([1, 2], [3, 4]), "y = do_something([1, 2], [3, 4])\nreturn y\n"
        )

    def test_with_underscore_param(self):
        @ancile_program
        def my_func(_param_name, _user="Sam"):
            _param_name = type(_user)

        self.assertEqual(my_func("param"), "param = type(Sam)\n")

    def test_with_gap_beggining(self):
        @ancile_program
        def my_func():

            return

        @ancile_program
        def another_func(_param, name, year=0, _type="test"):

            _param = type(name)

            return _param, year, _type

        self.assertEqual(my_func(), "return\n")

        self.assertEqual(
            another_func("first", "second", 43),
            "first = type('second')\nreturn first, 43, test\n",
        )

    def test_lists(self):
        @ancile_program
        def my_func(_my_list, another_list):
            print(_my_list)
            print(another_list)

        my_list = ["Sam", 1, "Hello"]

        self.assertEqual(
            my_func(my_list, my_list),
            "print([Sam, 1, Hello])\nprint(['Sam', 1, 'Hello'])\n",
        )

    def test_tuples(self):
        @ancile_program
        def my_func(_my_tuple, another_tuple):
            print(_my_tuple)
            print(another_tuple)

        my_tuple = ("Sam", 1, "Hello")

        self.assertEqual(
            my_func(my_tuple, my_tuple),
            "print((Sam, 1, Hello))\nprint(('Sam', 1, 'Hello'))\n",
        )


class TestBuildPrograms(unittest.TestCase):
    def test_onlyargs(self):

        first_case = [("Tim", 5), ("Another", 54)]
        second_case = (["Testing", 34], ["Testing #2", -32])

        @ancile_program
        def my_func(name, age):
            name + " " + str(age)

        self.assertEqual(
            build_programs(my_func, first_case),
            "'Tim' + \" \" + str(5)\n\n'Another' + \" \" + str(54)\n",
        )

        self.assertEqual(
            build_programs(my_func, second_case),
            "'Testing' + \" \" + str(34)\n\n'Testing #2' + \" \" + str(-32)\n",
        )
