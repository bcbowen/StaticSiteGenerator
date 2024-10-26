import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode
from text_type import TextType
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD.value)
        node2 = TextNode("This is a text node", TextType.BOLD.value)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD.value, "www.aol.com")
        node2 = TextNode("This is a text node", TextType.BOLD.value, "www.aol.com")
        self.assertEqual(node, node2)
    

    def test_neq_2_1(self):
        node = TextNode("This is a text node", TextType.BOLD.value)
        node2 = TextNode("This is a different text node", TextType.BOLD.value)
        self.assertNotEqual(node, node2)
    
    def test_neq2_2(self):
        node = TextNode("This is a text node", TextType.BOLD.value)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_neq3(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.aol.com")
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_node_to_html_text(self): 
        text = "This is text"
        node = TextNode(text, text_type=TextType.TEXT)
        expected = LeafNode(text)
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)

    def test_node_to_html_bold(self): 
        text = "I'm feeling quite bold!"
        node = TextNode(text = text, text_type=TextType.BOLD)
        expected = LeafNode(value=text, tag = "b")
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)

    def test_node_to_html_italic(self): 
        text = "Italics buddy"
        node = TextNode(text = text, text_type=TextType.ITALIC)
        expected = LeafNode(value=text, tag ="i")
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)      

    def test_node_to_html_code(self): 
        text = "10 goto 10"
        node = TextNode(text = text, text_type=TextType.CODE)
        expected = LeafNode(value=text, tag = TextType.CODE.value)
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)      

    def test_node_to_html_link(self): 
        text = "You got mail, dude"
        node = TextNode(text = text, text_type=TextType.LINK, url = "aol.com")
        expectedProps = {"href": "aol.com"}
        expected = LeafNode(value=text, tag = "a", props = expectedProps)
        result = TextNode.text_node_to_html_node(node)
        self.assertEqual(expected, result)   

    def test_node_to_html_img(self): 
        text = "breathtaking"
        node = TextNode(text = text, text_type=TextType.IMAGE, url = "aol.com")
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

    def test_link_text(self):
        test_cases = [
            ("to boot dev", "https://www.boot.dev", "[to boot dev](https://www.boot.dev)"), 
            ("to youtube", "https://www.youtube.com/@bootdotdev", "[to youtube](https://www.youtube.com/@bootdotdev)")
        ]

        for text, url, expected in test_cases: 
            with self.subTest(text = text, url = url, expected = expected):
                result = TextNode.get_link_text(text, url) 
                self.assertEqual(expected, result)

    def test_image_text(self):
        test_cases = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif", "![rick roll](https://i.imgur.com/aKaOqIh.gif)"), 
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg", "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        ]

        for text, url, expected in test_cases: 
            with self.subTest(text = text, url = url, expected = expected):
                result = TextNode.get_image_text(text, url) 
                self.assertEqual(expected, result)

    

if __name__ == "__main__":
    unittest.main()