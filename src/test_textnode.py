import unittest

from textnode import TextNode


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

if __name__ == "__main__":
    unittest.main()