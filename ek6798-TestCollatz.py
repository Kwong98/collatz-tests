#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_single_recursive

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):

    """unit test class: collatz"""
    # ----
    # read
    # ----

    def test_read_1(self):
        """unit test: collatz_read"""
        string = "1 10\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        """unit test: collatz_read"""
        string = "9999 44441\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 9999)
        self.assertEqual(j, 44441)

    def test_read_3(self):
        """unit test: collatz_read"""
        string = "999999 876543\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 999999)
        self.assertEqual(j, 876543)

    def test_read_4(self):
        """unit test: collatz_read"""
        string = "1 1\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """unit test: collatz_eval"""
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        """unit test: collatz_eval"""
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        """unit test: collatz_eval"""
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        """unit test: collatz_eval"""
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        """unit test: collatz_eval"""
        value = collatz_eval(999999, 836543)
        self.assertEqual(value, 525)

    def test_eval_6(self):
        """unit test: collatz_eval"""
        value = collatz_eval(999, 5040)
        self.assertEqual(value, 238)

    def test_eval_7(self):
        """unit test: collatz_eval"""
        value = collatz_eval(99999, 1000)
        self.assertEqual(value, 351)

    # ----------------
    # single_recursive
    # ----------------

    def test_single_recursive_1(self):
        """unit test: collatz_single_recursive"""
        value = collatz_single_recursive(1)
        self.assertEqual(value, 1)

    def test_single_recursive_2(self):
        """unit test: collatz_single_recursive"""
        value = collatz_single_recursive(100)
        self.assertEqual(value, 26)

    def test_single_recursive_3(self):
        """unit test: collatz_single_recursive"""
        value = collatz_single_recursive(210)
        self.assertEqual(value, 40)

    def test_single_recursive_4(self):
        """unit test: collatz_single_recursive"""
        value = collatz_single_recursive(837799)
        self.assertEqual(value, 525)

    def test_single_recursive_5(self):
        """unit test: collatz_single_recursive"""
        value = collatz_single_recursive(999999)
        self.assertEqual(value, 259)

    def test_single_recursive_6(self):
        """unit test: collatz_single_recursive"""
        value = collatz_single_recursive(5040)
        self.assertEqual(value, 42)

    def test_single_recursive_7(self):
        """unit test: collatz_single_recursive"""
        value = collatz_single_recursive(1000)
        self.assertEqual(value, 112)

    # -----
    # print
    # -----

    def test_print_1(self):
        """unit test: collatz_print"""
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """unit test: collatz_print"""
        writer = StringIO()
        collatz_print(writer, 999999, 1, 86666)
        self.assertEqual(writer.getvalue(), "999999 1 86666\n")

    def test_print_3(self):
        """unit test: collatz_print"""
        writer = StringIO()
        collatz_print(writer, 123456, 654321, 777666)
        self.assertEqual(writer.getvalue(), "123456 654321 777666\n")

    def test_print_4(self):
        """unit test: collatz_print"""
        writer = StringIO()
        collatz_print(writer, 1, 1, 1)
        self.assertEqual(writer.getvalue(), "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """unit test: collatz_solve"""
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """unit test: collatz_solve"""
        reader = StringIO("1 999999\n1 99999\n1 9999\n1 999\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "1 999999 525\n1 99999 351\n1 9999 262\n1 999 179\n")

    def test_solve_3(self):
        """unit test: collatz_solve"""
        reader = StringIO("8675 829999\n1 1\n7 1\n867530 9\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "8675 829999 509\n1 1 1\n7 1 17\n867530 9 525\n")

    def test_solve_4(self):
        """unit test: collatz_solve"""
        reader = StringIO("999999 1\n99999 1\n999 1\n2 1\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "999999 1 525\n99999 1 351\n999 1 179\n2 1 2\n")

    def test_solve_5(self):
        """unit test: collatz_solve"""
        reader = StringIO("\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
