"""
Test module for hello_world.py.

This module contains tests for the hello_world function.
"""

import unittest
from hello_world import hello_world


class TestHelloWorld(unittest.TestCase):
    """Test cases for the hello_world function."""
    
    def test_hello_world_returns_correct_string(self):
        """Test that hello_world returns the string 'Hello, World!'."""
        self.assertEqual(hello_world(), "Hello, World!")
    
    def test_hello_world_returns_string_type(self):
        """Test that hello_world returns a string type."""
        self.assertIsInstance(hello_world(), str)


if __name__ == "__main__":
    unittest.main()