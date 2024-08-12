import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_toString_with_tag(self):
        node = LeafNode(tag = 'a', props = {'target': 'self', 'href': 'https://www.aol.com'}, value = 'Click me man')
        result = str(node)
        expected = "<a target='self' href='https://www.aol.com'>Click me man</a>"
        self.assertEqual(expected, result)
    
    def test_toString_without_tag(self):
        node = LeafNode(value = 'Click me man')
        result = str(node)
        expected = "Click me man"
        self.assertEqual(expected, result)

    def test_leafnode_to_html(self):
        node = LeafNode(tag = 'a', props = {'target': 'self', 'href': 'https://www.aol.com'}, value = 'Click me man')
        result = node.to_html()
        expected = "<a target='self' href='https://www.aol.com'>Click me man</a>"
        self.assertEqual(expected, result)
    

if __name__ == "__main__":
    unittest.main()