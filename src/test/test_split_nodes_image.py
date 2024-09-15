import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode

class TestSplitNodesImage(unittest.TestCase):

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

    def test_split_nodes_one_image_middle(self): 
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image in the middle", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_image([node])
        expected =  [
            TextNode("This is text with a ",  TextNode.TEXT_TYPE_TEXT),
            TextNode("rick roll", TextNode.TEXT_TYPE_IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" image in the middle",  TextNode.TEXT_TYPE_TEXT)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_one_image_start(self): 
        node = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) image at the beginning", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_image([node])
        expected =  [
            TextNode("rick roll", TextNode.TEXT_TYPE_IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" image at the beginning",  TextNode.TEXT_TYPE_TEXT)
        ]

        self.assertEqual(new_nodes, expected)

    def test_split_nodes_one_image_end(self): 
        node = TextNode("Image at the end ![rick roll](https://i.imgur.com/aKaOqIh.gif) ", TextNode.TEXT_TYPE_TEXT)
        new_nodes = TextNode.split_nodes_image([node])
        expected =  [
            TextNode("Image at the end ",  TextNode.TEXT_TYPE_TEXT),
            TextNode("rick roll", TextNode.TEXT_TYPE_IMAGE, "https://i.imgur.com/aKaOqIh.gif")
        ]

        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()