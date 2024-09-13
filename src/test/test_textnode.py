import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", "bold", "www.aol.com")
        node2 = TextNode("This is a text node", "bold", "www.aol.com")
        self.assertEqual(node, node2)
    

    def test_neq_2_1(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node, node2)
    
    def test_neq2_2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    
    def test_neq3(self):
        node = TextNode("This is a text node", "bold", "www.aol.com")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node, node2)

    def test_node_to_html_text(self): 
        text = "This is text"
        node = TextNode(text, text_type="text")
        expected = LeafNode(value=text)
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)

    def test_node_to_html_bold(self): 
        text = "I'm feeling quite bold!"
        node = TextNode(text = text, text_type="bold")
        expected = LeafNode(value=text, tag = "b")
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)

    def test_node_to_html_italic(self): 
        text = "Italics buddy"
        node = TextNode(text = text, text_type="italic")
        expected = LeafNode(value=text, tag = "i")
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)      

    def test_node_to_html_code(self): 
        text = "10 goto 10"
        node = TextNode(text = text, text_type="code")
        expected = LeafNode(value=text, tag = "code")
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)      

    def test_node_to_html_link(self): 
        text = "You got mail, dude"
        node = TextNode(text = text, text_type="link", url = "aol.com")
        expectedProps = {"href": "aol.com"}
        expected = LeafNode(value=text, tag = "a", props = expectedProps)
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)   

    def test_node_to_html_img(self): 
        text = "breathtaking"
        node = TextNode(text = text, text_type="image", url = "aol.com")
        expectedProps = {"src": "aol.com", "alt": text}
        expected = LeafNode(value='', tag = "img", props = expectedProps)
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)                 

    def test_node_to_html_wrong_type_raisesError(self): 
        node = "I'm just a string"
        
        with self.assertRaises(Exception) as context:
            TextNode.text_node_to_html_node(node)
            self.assertTrue('invalid text node' in context.exception)

    def test_node_to_html_null_raisesError(self): 
        node = None
        
        with self.assertRaises(Exception) as context:
            TextNode.text_node_to_html_node(node)
            self.assertTrue('invalid text node' in context.exception)            

    def test_node_to_html_invalid_type_value_raisesError(self): 
        node = TextNode(text = "This is a node with a bad type", text_type="bad_type")
        
        with self.assertRaises(Exception) as context:
            TextNode.text_node_to_html_node(node)
            self.assertTrue('Invalid text type' in context.exception)  



if __name__ == "__main__":
    unittest.main()