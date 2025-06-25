"""
Unit tests for the hello_world module.
"""

import unittest
from hello_world import hello_world

class TestHelloWorld(unittest.TestCase):
    """Test cases for the hello_world function."""
    
    def test_hello_world_returns_correct_string(self):
        """Test that the hello_world function returns the expected string."""
        self.assertEqual(hello_world(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()