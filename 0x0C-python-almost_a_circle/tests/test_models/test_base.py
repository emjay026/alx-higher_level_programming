#!/usr/bin/python3
""" This module implements Unit Tests for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Unit Test class for Base class"""

    def test_Base_init(self):
        """ Test cases for Base class

            Method:
                __init__"""
        b1 = Base()
        b2 = Base()
        b3 = Base(13)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 13)
