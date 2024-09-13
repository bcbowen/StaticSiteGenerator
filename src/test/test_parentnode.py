import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_toString_with_one_child(self):
        children = [] 
        child = LeafNode(tag="b", value="Bold text")
        children.append(child)
        node = ParentNode(tag = 'p', children=children)
        result = str(node)
        expected = "<p><b>Bold text</b></p>"
        self.assertEqual(expected, result)
    
    def test_toString_with_two_kids(self):
        children = [] 
        child = LeafNode(tag="b", value="Bold text")
        children.append(child)
        child = LeafNode(value="Normal text")
        children.append(child)
        node = ParentNode(tag = 'p', children=children)
        result = str(node)
        expected = "<p><b>Bold text</b>Normal text</p>"
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()