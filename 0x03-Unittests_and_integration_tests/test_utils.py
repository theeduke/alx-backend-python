#!/usr/bin/env python3
"""
module for testing utils module
"""

import unittest
from unnittest.mock import patch, mock
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
     ({"a": 1}, ("a",), 1)),
     ({"a": {"b": 2}}, ("a",), {b:2}),
     ({"a": {"b": 2}},("a", "b"),2))
    ])
    def test_access_nested_map(self,nested_map, path, expected):
        self.asserEqual(access_nested_map, path), expected
    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
