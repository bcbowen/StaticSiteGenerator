import unittest

from htmlnode import HtmlNode


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
    

if __name__ == "__main__":
    unittest.main()