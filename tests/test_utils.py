import unittest
from ancile.utils import fix_gap, regex_repl_function, generate_url
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

class TestFixGenerateUrl(unittest.TestCase):

    def test_withslash(self):

        cases = [
            "https://ancile.cs.vassar.edu/",
            "http://localhost/",
            "http://127.0.0.1:5321/"
        ]

        expected_results = [
            "https://ancile.cs.vassar.edu/api/run",
            "http://localhost/api/run",
            "http://127.0.0.1:5321/api/run"
        ]

        for case, expected in zip(cases, expected_results):
            self.assertEqual(generate_url(case), expected)
    
    def test_withnoslash(self):

        cases = [
            "https://ancile.cs.vassar.edu",
            "http://localhost",
            "http://127.0.0.1:5321"
        ]

        expected_results = [
            "https://ancile.cs.vassar.edu/api/run",
            "http://localhost/api/run",
            "http://127.0.0.1:5321/api/run"
        ]

        for case, expected in zip(cases, expected_results):
            self.assertEqual(generate_url(case), expected)
