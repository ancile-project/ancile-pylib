import unittest
from ancile.utils import fix_gap, regex_repl_function
from ancile.programs import ancile_program

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

