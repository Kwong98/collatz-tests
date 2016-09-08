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

from Collatz import collatz_read, collatz_eval, collatz_step, collatz_cycle, collatz_print, collatz_solve

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
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 1)

    def test_read_3(self):
        s = "0 -99\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  0)
        self.assertEqual(j, -99)

    def test_read_4(self):
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  10)
        self.assertEqual(j, 1)

    def test_read_5(self):
        s = "\n"
        self.assertRaises(RuntimeError, collatz_read, s)

    def test_read_6(self):
        s = "1\n"
        self.assertRaises(RuntimeError, collatz_read, s)

    def test_read_7(self):
        s = "1 10 20\n"
        self.assertRaises(RuntimeError, collatz_read, s)
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

    def test_eval_4(self):
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)
    # ----
    # step
    # ----

    def test_step_1(self):
        n = collatz_step(2)
        self.assertEqual(n, 1)

    def test_step_2(self):
        n = collatz_step(3)
        self.assertEqual(n, 10)

    def test_step_3(self):
        n = collatz_step(20)
        self.assertEqual(n, 10)

    # -----
    # cycle
    # -----

    def test_cycle_1(self):
        n = collatz_cycle(1)
        self.assertEqual(n, 1)

    def test_cycle_2(self):
        n = collatz_cycle(5)
        self.assertEqual(n, 6)

    def test_cycle_3(self):
        n = collatz_cycle(10)
        self.assertEqual(n, 7)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

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
        r = StringIO("1 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n")

    def test_solve_3(self):
        r = StringIO("1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n")

    def test_solve_4(self):
        r = StringIO("10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n")

    def test_solve_5(self):
        r = StringIO("\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "")

    def test_solve_6(self):
        r = StringIO("1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "")

    def test_solve_7(self):
        r = StringIO("1 10 11\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "")


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
