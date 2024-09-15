import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_nodes_delimiter_code_block_middle(self): 
        node = TextNode("This is text with a `code block` word", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextNode.TEXT_TYPE_CODE)
        expected =  [
            TextNode("This is text with a ", TextNode.TEXT_TYPE_TEXT),
            TextNode("code block", TextNode.TEXT_TYPE_CODE),
            TextNode(" word", TextNode.TEXT_TYPE_TEXT)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_code_block_beginning(self): 
        node = TextNode("`code block` In the beginning", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextNode.TEXT_TYPE_CODE)
        expected =  [
            TextNode("code block", TextNode.TEXT_TYPE_CODE),
            TextNode(" In the beginning", TextNode.TEXT_TYPE_TEXT)
        ]

        self.assertEqual(new_nodes, expected)   

    def test_split_nodes_delimiter_code_block_end(self): 
        node = TextNode("In the end `code block`",TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextNode.TEXT_TYPE_CODE)
        expected =  [
            TextNode("In the end ", TextNode.TEXT_TYPE_TEXT),
            TextNode("code block", TextNode.TEXT_TYPE_CODE)
        ]

        self.assertEqual(new_nodes, expected)              

    def test_split_nodes_delimiter_code_block_multi(self): 
        node = TextNode("Multi `code blocks` here and `here`", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextNode.TEXT_TYPE_CODE)
        expected =  [
            TextNode("Multi ", TextNode.TEXT_TYPE_TEXT),
            TextNode("code blocks", TextNode.TEXT_TYPE_CODE),
            TextNode(" here and ", TextNode.TEXT_TYPE_TEXT),
            TextNode("here", TextNode.TEXT_TYPE_CODE)
        ]

        self.assertEqual(new_nodes, expected) 

    def test_split_nodes_delimiter_italic_block_middle(self): 
        node = TextNode("This is text with an *italic block* word", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextNode.TEXT_TYPE_CODE)
        expected =  [
            TextNode("This is text with an ", TextNode.TEXT_TYPE_TEXT),
            TextNode("italic block", TextNode.TEXT_TYPE_CODE),
            TextNode(" word", TextNode.TEXT_TYPE_TEXT)
        ]

    def test_split_nodes_delimiter_bold_block_middle(self): 
        node = TextNode("This is text with a **bold block** word", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextNode.TEXT_TYPE_CODE)
        expected =  [
            TextNode("This is text with a ", TextNode.TEXT_TYPE_TEXT),
            TextNode("bold block", TextNode.TEXT_TYPE_CODE),
            TextNode(" word", TextNode.TEXT_TYPE_TEXT)
        ]

if __name__ == "__main__":
    unittest.main()