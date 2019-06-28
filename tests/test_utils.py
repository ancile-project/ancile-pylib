import unittest
from ancile.utils import build_programs, fix_gap, regex_repl_function
from ancile.wrappers import ancile_program

class TestFixGap(unittest.TestCase):

    def test_nogap(self):

        first_case = ["return x"]
        second_case = ["    def my_func_second():\n", "        return \"nest\""]

        self.assertEqual(fix_gap(first_case), "return x")

        self.assertEqual(
            fix_gap(second_case),
            "def my_func_second():\n    return \"nest\"")

    def test_manygaps(self):
        first_case = ["        return x"]

        second_case = ["            def my_func_second():\n",
                       "                return \"nest\""]

        self.assertEqual(fix_gap(first_case), "return x")

        self.assertEqual(
            fix_gap(second_case),
            "def my_func_second():\n    return \"nest\"")

class TestBuildPrograms(unittest.TestCase):

    def test_onlyargs(self):

        first_case = [("Tim", 5), ("Another", 54)]
        second_case = (["Testing", 34], ["Testing #2", -32])

        @ancile_program
        def my_func(name, age):
            name + " " + str(age)

        self.assertEqual(build_programs(my_func, first_case),
                         "'Tim' + \" \" + str(5)\n\n'Another' + \" \" + str(54)\n")

        self.assertEqual(build_programs(my_func, second_case),
                         "'Testing' + \" \" + str(34)\n\n'Testing #2' + \" \" + str(-32)\n")
