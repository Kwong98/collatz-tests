#!/usr/bin/env python3.5

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length, get_meta_cache_max

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1(self):
        n = 9
        c = collatz_cycle_length(n)
        self.assertEqual(c, 20)
    
    def test_cycle_length_2(self):
        n = 100000
        c = collatz_cycle_length(n)
        self.assertEqual(c, 129)
    
    def test_cycle_length_3(self):
        n = 128
        c = collatz_cycle_length(n)
        self.assertEqual(c, 8)

    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "100 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(i, 100)

    def test_read_3(self):
        s = "1000 2000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1000)
        self.assertEqual(j, 2000)

    # --------------
    # meta_cache_max
    # --------------

    def test_meta_cache_max_1(self):
        m = get_meta_cache_max(1001, 1002)
        self.assertEqual(m, 0)
        
    def test_meta_cache_max_2(self):
        m = get_meta_cache_max(1001, 2001)
        self.assertEqual(m, 0)
    
    def test_meta_cache_max_3(self):
        m = get_meta_cache_max(1001, 3001)
        self.assertEqual(m, 217) # cache[2] == 217

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_1b(self):
        v = collatz_eval(10, 1)
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
        v = collatz_eval(2, 2)
        self.assertEqual(v, 2)
    
    def test_eval_6(self):
        v = collatz_eval(1000, 3000)
        self.assertEqual(v, 217)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 10, 100, 200)
        self.assertEqual(w.getvalue(), "10 100 200\n")
    
    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 100, 1000, 2000)
        self.assertEqual(w.getvalue(), "100 1000 2000\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n1\n\n100 200\n201 210\n900 1000\n")
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
        r = StringIO("201 210\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "201 210 89\n")

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
