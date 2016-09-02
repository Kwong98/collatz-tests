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
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "9 8\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 9)
        self.assertEqual(j, 8)

    def test_read_3(self):
        s = "-5 7\n"
        i, j = collatz_read(s)
        self.assertEqual(i, -5)
        self.assertEqual(j, 7)

    def test_read_4(self):
        s = "0 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 0)

    # ----
    # getMaxCycleLength helper tests
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
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)

    def test_eval_6(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_7(self):
        v = collatz_eval(10, 7)
        self.assertEqual(v, 20)

    def test_eval_8(self):
        v = collatz_eval(13, 17)
        self.assertEqual(v, 18)

    #---------
    # eval cache testing
    #---------

    def test_eval_9(self):
        v = collatz_eval(1, 10000)
        self.assertEqual(v, 262)

    def test_eval_10(self):
        v = collatz_eval(990000, 1000000)
        self.assertEqual(v, 440)

    def test_eval_11(self):
        v = collatz_eval(1, 1000000)
        self.assertEqual(v, 525)

    def test_eval_12(self):
        v = collatz_eval(5000, 15000)
        self.assertEqual(v, 276)

    def test_eval_13(self):
        v = collatz_eval(5000, 25000)
        self.assertEqual(v, 282)

    def test_eval_14(self):
        v = collatz_eval(1, 15000)
        self.assertEqual(v, 276)

    def test_eval_15(self):
        v = collatz_eval(5000, 20000)
        self.assertEqual(v, 279)

    def test_eval_16(self):
        v = collatz_eval(10000, 15000)
        self.assertEqual(v, 276)

    def test_eval_17(self):
        v = collatz_eval(15000, 20000)
        self.assertEqual(v, 279)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, -5, 7, 14)
        self.assertEqual(w.getvalue(), "-5 7 14\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 1\n17 13\n10 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n17 13 18\n10 10 7\n")

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
