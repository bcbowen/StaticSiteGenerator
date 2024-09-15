import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode

class TestSplitNodesLink(unittest.TestCase):

    def test_text_to_textnodes(self): 
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = TextNode.text_to_textnodes(text)
        expected =  [
            TextNode("This is ", TextNode.TEXT_TYPE_TEXT),
            TextNode("text", TextNode.TEXT_TYPE_BOLD),
            TextNode(" with an ", TextNode.TEXT_TYPE_TEXT),
            TextNode("italic", TextNode.TEXT_TYPE_ITALIC),
            TextNode(" word and a ", TextNode.TEXT_TYPE_TEXT),
            TextNode("code block", TextNode.TEXT_TYPE_CODE),
            TextNode(" and an ", TextNode.TEXT_TYPE_TEXT),
            TextNode("obi wan image", TextNode.TEXT_TYPE_IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextNode.TEXT_TYPE_TEXT),
            TextNode("link", TextNode.TEXT_TYPE_LINK, "https://boot.dev")
        ]
        self.assertEqual(expected, new_nodes)



if __name__ == "__main__":
    unittest.main()