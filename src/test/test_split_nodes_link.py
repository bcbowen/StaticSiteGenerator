import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode

class TestSplitNodesLink(unittest.TestCase):

    """
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        text_type_text,
    )
    new_nodes = split_nodes_link([node])
    # [
    #     TextNode("This is text with a link ", text_type_text),
    #     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
    #     TextNode(" and ", text_type_text),
    #     TextNode(
    #         "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
    #     ),
    # ]

    def test_extract_markdown_images(self): 
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = TextNode.extract_markdown_images(text)
        self.assertEqual(expected, result)


    """

    def test_split_nodes_one_link_middle(self): 
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) in the middle", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_link([node])
        expected =  [
            TextNode("This is text with a link ",  TextNode.TEXT_TYPE_TEXT),
            TextNode("to boot dev", TextNode.TEXT_TYPE_LINK, "https://www.boot.dev"),
            TextNode(" in the middle",  TextNode.TEXT_TYPE_TEXT)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_one_link_start(self): 
        node = TextNode("[to boot dev](https://www.boot.dev) link at the beginning", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_link([node])
        expected =  [
            TextNode("to boot dev", TextNode.TEXT_TYPE_LINK, "https://www.boot.dev"),
            TextNode(" link at the beginning",  TextNode.TEXT_TYPE_TEXT)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_one_link_start(self): 
        node = TextNode("Link at the end [to boot dev](https://www.boot.dev)", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_link([node])
        expected =  [
            TextNode("Link at the end ",  TextNode.TEXT_TYPE_TEXT),
            TextNode("to boot dev", TextNode.TEXT_TYPE_LINK, "https://www.boot.dev")
        ]

        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()