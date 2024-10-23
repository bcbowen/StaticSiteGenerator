import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from htmlnode import HtmlNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_toString_with_val(self):
        node = HtmlNode(tag = 'a', props = {'target': 'self', 'href': 'https://www.aol.com'}, value = 'Click me man')
        result = str(node)
        expected = "<a target='self' href='https://www.aol.com'>Click me man</a>"
        self.assertEqual(expected, result)
    
    def test_toString_with_children(self):
        children = [];
        children.append(HtmlNode(tag = 'li', value = 'first'))
        children.append(HtmlNode(tag = 'li', value = 'second'))
        node = HtmlNode(tag = 'ul', children = children)
        result = str(node)
        expected = "<ul><li>first</li><li>second</li></ul>"
        self.assertEqual(expected, result)

    def test_props_to_html(self):
        node = HtmlNode(tag = 'a', props = {'target': 'self', 'href': 'https://www.aol.com'}, value = 'Click me man')
        result = node.props_to_html()
        expected = " target='self' href='https://www.aol.com'"
        self.assertEqual(expected, result)
    
    def test_to_html_props(self):
        node = HtmlNode(
            tag="div",
            value="Hello, world!",
            children=None,
            props={"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            " class='greeting' href='https://boot.dev'",
        )

    def test_values(self):
        node = HtmlNode(
            tag="div",
            value="I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HtmlNode(
            tag="p",
            value="What a strange world",
            children=None,
            props={"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "<p class='primary'>What a strange world</p>",
        )

    def test_to_html_no_children(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(tag=None, value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode(tag="span", value="child")
        parent_node = ParentNode(tag="div", children=[child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode(tag="b", value="grandchild")
        child_node = ParentNode(tag="span", children=[grandchild_node])
        parent_node = ParentNode(tag="div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()