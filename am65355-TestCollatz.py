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


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "  1   10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "   4          4   \n"
        i, j = collatz_read(s)
        self.assertEqual(i,  4)
        self.assertEqual(j,  4)

    def test_read_3(self):
        s = " 44  1     \n"
        i, j = collatz_read(s)
        self.assertEqual(i, 44)
        self.assertEqual(j,  1)

    def test_read_4(self):
        s = "    930 52    \n"
        i, j = collatz_read(s)
        self.assertEqual(i, 930)
        self.assertEqual(j,  52)

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
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_6(self):
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_7(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_8(self):
        v = collatz_eval(660357, 203881)
        self.assertEqual(v, 509)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 302, 103, 128)
        self.assertEqual(w.getvalue(), "302 103 128\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 7, 143, 122)
        self.assertEqual(w.getvalue(), "7 143 122\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 78, 13, 116)
        self.assertEqual(w.getvalue(), "78 13 116\n")

    def test_print_5(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print_6(self):
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    # ----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO(
            "831197 818578\n287963 315971\n736321 680328\n249040 773148\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "831197 818578 450\n287963 315971 389\n736321 680328 504\n249040 773148 509\n")

    def test_solve_3(self):
        r = StringIO(
            "427643 682576\n413598 254022\n161128 223470\n197236 839150\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "427643 682576 509\n413598 254022 449\n161128 223470 386\n197236 839150 525\n")


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
