import unittest
from ancile.utils import fix_gap, regex_repl_function

class TestFixGap(unittest.TestCase):

    def test_nogap(self):

        first_case = '''@ancile_function
def my_func():
    return x
'''

        second_case = '''@ancile_function
def my_func():
    def my_func_second():
        return "nest"
'''

        self.assertEqual(
            fix_gap(first_case),
            '''@ancile_function
def my_func():
    return x
'''
        )

        self.assertEqual(
            fix_gap(second_case),
            '''@ancile_function
def my_func():
    def my_func_second():
        return "nest"
'''
        )
    
    def test_manygaps(self):
        first_case = '''    @ancile_function
    def my_func():
        return x
'''

        second_case = '''       @ancile_function
        def my_func():
            def my_func_second():
                return "nest"
'''
        
        self.assertEqual(
            fix_gap(first_case),
            '''    @ancile_function
def my_func():
    return x
'''
        )

        self.assertEqual(
            fix_gap(second_case),
            '''       @ancile_function
def my_func():
    def my_func_second():
        return "nest"
'''
        )
