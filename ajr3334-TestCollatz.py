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

# ------------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # Test the case where only a single number is passed in
    def test_read_2(self):
        s = "10"
        i, j = collatz_read(s)
        self.assertEqual(i, -1)
        self.assertEqual(j, -1)

    # Test if an empty string is passed in
    def test_read_3(self):
        s = ""
        i, j = collatz_read(s)
        self.assertEqual(i, -1)
        self.assertEqual(j, -1)

    # Test a bunch of empty spaces
    def test_read_4(self):
        s = "       "
        i, j = collatz_read(s)
        self.assertEqual(i, -1)
        self.assertEqual(j, -1)

    # Check the case where there are 2 items, but aren't numbers
    def test_read_5(self):
        s = "a b"
        i, j = collatz_read(s)
        self.assertEqual(i, -1)
        self.assertEqual(j, -1)

    # Check the case where there are decimals
    def test_read_6(self):
        s = "10.3 1.12"
        i, j = collatz_read(s)
        self.assertEqual(i, -1)
        self.assertEqual(j, -1)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(-1, -1)
        self.assertEqual(v, -1)

    def test_eval_6(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_7(self):
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, -1, -1, -1)
        self.assertEqual(w.getvalue(), '')
    
    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # Test for just a single number in a linee
    def test_solve_1(self):
        r = StringIO("1 10\n200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n201 210 89\n900 1000 174\n")

    # Test for a line with just space/empty line
    def test_solve_2(self):
        r = StringIO("1 10\n \n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n201 210 89\n900 1000 174\n")



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
