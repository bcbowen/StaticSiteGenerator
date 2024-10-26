import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode
from text_type import TextType

class TestSplitNodesImage(unittest.TestCase):


    def test_split_nodes_one_image_middle(self): 
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image in the middle", TextType.TEXT)
        new_nodes = TextNode.split_nodes_image([node])
        expected =  [
            TextNode("This is text with a ",  TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" image in the middle",  TextType.TEXT)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_one_image_start(self): 
        node = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) image at the beginning", TextType.TEXT)
        new_nodes = TextNode.split_nodes_image([node])
        expected =  [
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" image at the beginning",  TextType.TEXT)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_one_image_end(self): 
        node = TextNode("Image at the end ![rick roll](https://i.imgur.com/aKaOqIh.gif) ", TextType.TEXT)
        new_nodes = TextNode.split_nodes_image([node])
        expected =  [
            TextNode("Image at the end ",  TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif")
        ]

        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()