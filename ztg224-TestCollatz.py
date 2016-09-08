#!/usr/bin/env python3.5
"""
Test Module for Collatz.
"""

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------
# pylint: disable=R0904, C0301

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, eval_recursive

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """
    Test Class for Collatz.
    """
    # ----
    # read
    # ----

    def test_read1(self):
        """
        Testing basic input.
        """
        string = "1 10\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, 1)
        self.assertEqual(end, 10)

    def test_read2(self):
        """
        Testing empty line.
        """
        string = "\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, -1)
        self.assertEqual(end, -1)

    def test_read3(self):
        """
        Testing whitespace line.
        """
        string = "  \n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, -1)
        self.assertEqual(end, -1)

    def test_eval_recursive1(self):
        "Testing eval for single number"
        self.assertEqual(20, eval_recursive(9))

    def test_eval_recursive2(self):
        "Testing eval for single number"
        self.assertEqual(112, eval_recursive(27))

    def test_eval_recursive3(self):
        "Testing eval for single number"
        self.assertEqual(54, eval_recursive(98765))

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Testing basic input.
        """
        max_cl = collatz_eval(1, 10)
        self.assertEqual(max_cl, 20)

    def test_eval_2(self):
        """
        Testing large inverse input.
        """
        max_cl = collatz_eval(44008, 6990)
        self.assertEqual(max_cl, 324)

    def test_eval_3(self):
        """
        Testing large input with large cycle length.
        """
        max_cl = collatz_eval(525677, 527500)
        self.assertEqual(max_cl, 408)

    # -----
    # print
    # -----

    def test_print1(self):
        """
        Testing basic output.
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print2(self):
        """
        Testing basic output with inversed range.
        """
        writer = StringIO()
        collatz_print(writer, 44008, 6990, 324)
        self.assertEqual(writer.getvalue(), "44008 6990 324\n")

    def test_print3(self):
        """
        Testing basic output with large nombres.
        """
        writer = StringIO()
        collatz_print(writer, 525677, 527500, 408)
        self.assertEqual(writer.getvalue(), "525677 527500 408\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        """
        Testing basic input and output.
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        """
        Testing complex input and output.
        """
        reader = StringIO("1 10\n44008 6990\n525677 527500\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n44008 6990 324\n525677 527500 408\n")

    def test_solve3(self):
        """
        Testing complex input and output with empty line.
        """
        reader = StringIO("1 10\n\n525677 527500\n44008 6990\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n525677 527500 408\n44008 6990 324\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
