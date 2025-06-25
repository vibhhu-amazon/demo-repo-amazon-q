"""
Test module for hello_world.py
"""

import unittest
import io
import sys
from hello_world import hello_world

class TestHelloWorld(unittest.TestCase):
    """Test cases for the hello_world function."""
    
    def test_hello_world_return_value(self):
        """Test that hello_world returns the correct string."""
        result = hello_world()
        self.assertEqual(result, "Hello, World!")
    
    def test_hello_world_prints_correctly(self):
        """Test that hello_world prints the correct string to stdout."""
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the function
        hello_world()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the captured output
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()