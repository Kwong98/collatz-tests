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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        line = "1 10\n"
        start, end = collatz_read(line)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        value = collatz_eval(1, 2)
        self.assertEqual(value, 2)

    def test_eval_6(self):
        value = collatz_eval(10, 1)
        self.assertEqual(value, 20)

    def test_eval_7(self):
        value = collatz_eval(10, 1)
        self.assertEqual(value, 20)

    def test_eval_8(self):
        value = collatz_eval(42, 1042)
        self.assertEqual(value, 179)

    def test_eval_9(self):
        value = collatz_eval(1, 985362)
        self.assertEqual(value, 525)

    def test_eval_10(self):
        value = collatz_eval(999999, 1)
        self.assertEqual(value, 525)


    # -----
    # print
    # -----

    def test_print(self):
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), 
            "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        reader = StringIO("1 10\n\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), 
            "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_3(self):
        reader = StringIO("1 10\n5 \n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), 
            "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
