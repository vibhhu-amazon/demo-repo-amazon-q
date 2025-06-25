"""
Test module for hello.py
"""
import unittest
from hello import hello_world

class TestHelloWorld(unittest.TestCase):
    """Test cases for the hello_world function."""
    
    def test_hello_world(self):
        """Test that hello_world returns the expected string."""
        self.assertEqual(hello_world(), "Hello, World!")
        
    def test_hello_world_type(self):
        """Test that hello_world returns a string."""
        self.assertIsInstance(hello_world(), str)

if __name__ == "__main__":
    unittest.main()