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

    def test_read(self):
        s = "11 610\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 11)
        self.assertEqual(j, 610)

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

    def test_eval_5(self):      # test two identical numbers
        v = collatz_eval(7, 7)
        self.assertEqual(v, 17)

    def test_eval_6(self):      # test two identical numbers at low edge
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_7(self):      # test two identical numbers at high edge
        v = collatz_eval(999999, 999999)
        self.assertEqual(v, 259)

    def test_eval_8(self):      # test two sequential numbers
        v = collatz_eval(7, 8)
        self.assertEqual(v, 17)

    def test_eval_9(self):      # test numbers in the wrong order
        v = collatz_eval(4, 2)
        self.assertEqual(v, 8)

    def test_eval_10(self):      # test large range
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)


    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 78, 200)
        self.assertEqual(w.getvalue(), "1 78 200\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

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
