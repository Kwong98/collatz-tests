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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length, max_cycle

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # cycle_length
    # ----

    def test_cycle_length_1(self):
        i = cycle_length(2815)
        self.assertEqual(i, 160)

    def test_cycle_length_2(self):
        i = cycle_length(149875)
        self.assertEqual(i, 189)

    def test_cycle_length_3(self):
        i = cycle_length(568219)
        self.assertEqual(i, 129)

    # ----
    # max_cycle
    #  ----

    def test_max_cycle_1(self):
        i = max_cycle(126872, 127999)
        self.assertEqual(i, 300)

    def test_max_cycle_2(self):
        i = max_cycle(59968, 79067)
        self.assertEqual(i, 351)

    def test_max_cycle_3(self):
        i = max_cycle(219314, 225912)
        self.assertEqual(i, 368)

    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "281722 19393\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 281722)
        self.assertEqual(j, 19393)

    def test_read_3(self):
        s = "12345 54321\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 12345)
        self.assertEqual(j, 54321)

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
        v = collatz_eval(32827, 40932)
        self.assertEqual(v, 324)

    def test_eval_6(self):
        v = collatz_eval(70524, 49704)
        self.assertEqual(v, 340)

    def test_eval_7(self):
        v = collatz_eval(657529, 658805)
        self.assertEqual(v, 398)

    def test_eval_8(self):
        v = collatz_eval(17296, 3520)
        self.assertEqual(v, 276)

    def test_eval_9(self):
        v = collatz_eval(69265, 90163)
        self.assertEqual(v, 351)

    def test_eval_10(self):
        v = collatz_eval(41809, 88621)
        self.assertEqual(v, 351)

    def test_eval_11(self):
        v = collatz_eval(988852, 990763)
        self.assertEqual(v, 352)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 16287, 27662, 308)
        self.assertEqual(w.getvalue(), "16287 27662 308\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 102994, 101780, 310)
        self.assertEqual(w.getvalue(), "102994 101780 310\n")

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
        r = StringIO("2888 70826\n37926 109066\n75518 107722\n659896 663701\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "2888 70826 340\n37926 109066 354\n75518 107722 354\n659896 663701 323\n")

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
