import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode

class TestSplitNodesDelimiter(unittest.TestCase):


    text_type_text="text"
    text_type_code="code"

    def test_split_nodes_delimiter_code_block_middle(self): 
        node = TextNode("This is text with a `code block` word", TestSplitNodesDelimiter.text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TestSplitNodesDelimiter.text_type_code)
        expected =  [
            TextNode("This is text with a ", TestSplitNodesDelimiter.text_type_text),
            TextNode("code block", TestSplitNodesDelimiter.text_type_code),
            TextNode(" word", TestSplitNodesDelimiter.text_type_text)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_code_block_beginning(self): 
        node = TextNode("`code block` In the beginning", TestSplitNodesDelimiter.text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TestSplitNodesDelimiter.text_type_code)
        expected =  [
            TextNode("code block", TestSplitNodesDelimiter.text_type_code),
            TextNode(" In the beginning", TestSplitNodesDelimiter.text_type_text)
        ]

        self.assertEqual(new_nodes, expected)   

    def test_split_nodes_delimiter_code_block_end(self): 
        node = TextNode("In the end `code block`", TestSplitNodesDelimiter.text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TestSplitNodesDelimiter.text_type_code)
        expected =  [
            TextNode("In the end ", TestSplitNodesDelimiter.text_type_text),
            TextNode("code block", TestSplitNodesDelimiter.text_type_code)
        ]

        self.assertEqual(new_nodes, expected)              

    def test_split_nodes_delimiter_code_block_multi(self): 
        node = TextNode("Multi `code blocks` here and `here`", TestSplitNodesDelimiter.text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TestSplitNodesDelimiter.text_type_code)
        expected =  [
            TextNode("Multi ", TestSplitNodesDelimiter.text_type_text),
            TextNode("code blocks", TestSplitNodesDelimiter.text_type_code),
            TextNode(" here and ", TestSplitNodesDelimiter.text_type_text),
            TextNode("here", TestSplitNodesDelimiter.text_type_code)
        ]

        self.assertEqual(new_nodes, expected) 

    def test_split_nodes_delimiter_italic_block_middle(self): 
        node = TextNode("This is text with an *italic block* word", TestSplitNodesDelimiter.text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TestSplitNodesDelimiter.text_type_code)
        expected =  [
            TextNode("This is text with an ", TestSplitNodesDelimiter.text_type_text),
            TextNode("italic block", TestSplitNodesDelimiter.text_type_code),
            TextNode(" word", TestSplitNodesDelimiter.text_type_text)
        ]

    def test_split_nodes_delimiter_bold_block_middle(self): 
        node = TextNode("This is text with a **bold block** word", TestSplitNodesDelimiter.text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TestSplitNodesDelimiter.text_type_code)
        expected =  [
            TextNode("This is text with a ", TestSplitNodesDelimiter.text_type_text),
            TextNode("bold block", TestSplitNodesDelimiter.text_type_code),
            TextNode(" word", TestSplitNodesDelimiter.text_type_text)
        ]

if __name__ == "__main__":
    unittest.main()