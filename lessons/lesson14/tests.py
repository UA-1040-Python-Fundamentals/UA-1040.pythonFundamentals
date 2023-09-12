from unittest import TestCase

from func import my_sort
import inspect


class MySortTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("\tsetUp")
    def tearDown(self) -> None:
        print("\ttearDown")

    def test_ok(self):
        print("\t"*2, inspect.currentframe().f_code.co_name)

        data = [1, 2, 4, 2, 3, 6, 3, 4, 6]
        actual = my_sort(data)
        expected = [1, 2, 2, 3, 3, 4, 4, 6, 6]
        self.assertEquals(actual, expected)

    def test_fail(self):
        print("\t" * 3, inspect.currentframe().f_code.co_name)
        data = [1, 2, 4, 2, 3, 6, 3, 4, 6, 5]
        actual = my_sort(data)
        expected = [1, 2, 2, 3, 3, 4, 4, 6, 6]
        self.assertEquals(actual, expected)

    def test_list_int_str(self):
        print("\t"*3, inspect.currentframe().f_code.co_name)
        data = [1, 2, 4, "2", 3, 6, "3", "4", 6]
        actual = my_sort(data, key=lambda e: int(e))
        expected = [1, 2, '2', 3, '3', 4, '4', 6, 6]
        self.assertEquals(actual, expected)
