import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode

class TestSplitNodesLink(unittest.TestCase):
    def test_split_blocks(self):
        """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        doc = "# This is a heading \n"\
        "\n"\
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"\
        "\n"\
        "* This is the first list item in a list block\n"\
        "* This is a list item\n"\
        "* This is another list item\n"
        expected = []
        expected.append("# This is a heading ")
        expected.append("This is a paragraph of text. It has some **bold** and *italic* words inside of it.")
        expected.append("* This is the first list item in a list block"\
        "* This is a list item"\
        "* This is another list item")

        result = TextNode.markdown_to_blocks(doc)
        self.assertEqual(expected, result)


    
if __name__ == "__main__":
    unittest.main()