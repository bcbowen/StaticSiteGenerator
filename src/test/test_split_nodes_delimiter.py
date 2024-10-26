import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode
from text_type import TextType

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_nodes_delimiter_code_block_middle(self): 
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        expected =  [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_code_block_beginning(self): 
        node = TextNode("`code block` In the beginning", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        expected =  [
            TextNode("code block", TextType.CODE),
            TextNode(" In the beginning", TextType.TEXT)
        ]

        self.assertEqual(new_nodes, expected)   

    def test_split_nodes_delimiter_code_block_end(self): 
        node = TextNode("In the end `code block`",TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        expected =  [
            TextNode("In the end ", TextType.TEXT),
            TextNode("code block", TextType.CODE)
        ]

        self.assertEqual(new_nodes, expected)              

    def test_split_nodes_delimiter_code_block_multi(self): 
        node = TextNode("Multi `code blocks` here and `here`", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        expected =  [
            TextNode("Multi ", TextType.TEXT),
            TextNode("code blocks", TextType.CODE),
            TextNode(" here and ", TextType.TEXT),
            TextNode("here", TextType.CODE)
        ]

        self.assertEqual(new_nodes, expected) 

    def test_split_nodes_delimiter_italic_block_middle(self): 
        node = TextNode("This is text with an *italic block* word", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        expected =  [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]

    def test_split_nodes_delimiter_bold_block_middle(self): 
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        expected =  [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]

if __name__ == "__main__":
    unittest.main()