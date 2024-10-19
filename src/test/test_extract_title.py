import sys
import os 
import unittest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import extract_title

class TestExtractTitle(unittest.TestCase): 

    def test_link_text(self):
        md1 = "# Hey Buddy!\n" \
        " * here's a bullet\n" \
        " 1 and an ordered list\n"

        md2 = " This one is a little \n" \
        "# Sneaky \n" \
        "**right?**\n"
        
        test_cases = [
            (md1, "Hey Buddy!"), 
            (md2, "Sneaky")
        ]

        for md, expected in test_cases: 
            with self.subTest(md = md, expected = expected):
                result = extract_title(md) 
                self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()