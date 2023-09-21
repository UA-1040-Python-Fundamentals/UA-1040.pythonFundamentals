from functions import *
import unittest


class TestGreetingByName(unittest.TestCase):

    def test_greeting_with_name(self):
        name = "Kolya"
        result = greeting_by_name(name)
        self.assertEqual(result, "Hello Kolya!")

    def test_greeting_without_name(self):
        name = ""
        result = greeting_by_name(name)
        self.assertEqual(result, "Hello !")


class TestGetSymbolPosition(unittest.TestCase):

    def test_single_symbol_in_text(self):
        text = "Hello, world!"
        symbol = "!"
        result = get_symbol_position(text, symbol)
        self.assertEqual(result, 13) 

    def test_symbol_not_in_text(self):
        text = "Hello, world!"
        symbol = "k"
        result = get_symbol_position(text, symbol)
        self.assertEqual(result, "Not found")

    def test_multiple_symbols(self):
        text = "Hello, world!"
        symbol = "wo"
        result = get_symbol_position(text, symbol)
        self.assertEqual(result, "Error! Symbol can be string with only one letter") 


class TestMerge(unittest.TestCase):

    def test_merge_dicts(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected_result = {'a': 1, 'b': 3, 'c': 4}
        result = merge(dict1, dict2)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()