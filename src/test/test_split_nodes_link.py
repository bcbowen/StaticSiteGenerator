import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode
from text_type import TextType

class TestSplitNodesLink(unittest.TestCase):

    def test_split_nodes_one_link_middle(self): 
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) in the middle", TextType.TEXT)
        new_nodes = TextNode.split_nodes_link([node])
        expected =  [
            TextNode("This is text with a link ",  TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" in the middle",  TextType.TEXT)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_one_link_start(self): 
        node = TextNode("[to boot dev](https://www.boot.dev) link at the beginning", TextType.TEXT)
        new_nodes = TextNode.split_nodes_link([node])
        expected =  [
            TextNode("to boot dev", TextNode.TEXT_TYPE_LINK, "https://www.boot.dev"),
            TextNode(" link at the beginning",  TextType.TEXT)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_one_link_start(self): 
        node = TextNode("Link at the end [to boot dev](https://www.boot.dev)", TextType.TEXT)
        new_nodes = TextNode.split_nodes_link([node])
        expected =  [
            TextNode("Link at the end ",  TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        ]

        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()