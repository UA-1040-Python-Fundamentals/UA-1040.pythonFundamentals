import unittest
from functions import greeting_by_name as greeting_by_name_correct
from functions import get_symbol_position as get_symbol_position_correct
from functions import merge as merge_correct

from functions_with_errors import greeting_by_name, get_symbol_position, merge


class TestFunctions(unittest.TestCase):
    def test_greeting_by_name(self):
        name = "Alice"

        # Test the correct function from functions.py
        result_correct = greeting_by_name_correct(name)
        self.assertEqual(result_correct, f"Hello {name}!")

        # Test the function with errors from functions_with_errors.py
        result_with_errors = greeting_by_name(name)
        self.assertEqual(result_with_errors, f"Hello name!")  # This should fail

    def test_get_symbol_position(self):
        text = "Hello, World!"
        symbol = "o"

        # Test the correct function from functions.py
        result_correct = get_symbol_position_correct(text, symbol)
        self.assertEqual(result_correct, 5)

        # Test the function with errors from functions_with_errors.py
        result_with_errors = get_symbol_position(text, symbol)
        self.assertEqual(result_with_errors, text.find(symbol))  # This should fail

    def test_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}

        # Test the correct function from functions.py
        result_correct = merge_correct(dict1.copy(), dict2.copy())
        self.assertEqual(result_correct, {'a': 1, 'b': 3, 'c': 4})

        # Test the function with errors from functions_with_errors.py
        result_with_errors = merge(dict1.copy(), dict2.copy())
        self.assertEqual(result_with_errors, {'a': 1, 'b': 3, 'c': 4})  # This should fail


if __name__ == '__main__':
    unittest.main()
