import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from markdown_blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node, block_type_paragraph, block_type_code, block_type_heading, block_type_olist, block_type_quote, block_type_ulist

"""
These tests borrowed and adapted from the course tests to help troubleshoot a few issues with my implementation 
"""

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is a code block
```

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is a code block</code></pre><p>this is paragraph text</p></div>",
        )

def test_block_to_blocktype(self):

        test_cases = [
            ("This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "paragraph"),
            ("**I am bold** This is a paragraph.", "paragraph"),
            ("# This is a heading", "heading"), 
            (" ## This is a heading", "heading"), 
            ("### This is a heading", "heading"), 
            ("  #### This is a heading", "heading"), 
            ("##### This is a heading", "heading"), 
            ("###### This is a heading", "heading"), 
            ("####### This is not a heading", "paragraph"),
            ("#This is not a heading", "paragraph"),

            ("```<p>Code block</p>```", "code"),
            ("``<p>Not a code block</p>```", "paragraph"),
            ("```<p>Not a code block</p>``", "paragraph"),
            ("``<p>Not a code block</p>``", "paragraph"),
            ("```<p>Not a code block</p>", "paragraph"),

            ("> The dude abides", "quote"),

            ("* This is an unordered list", "unordered_list"),
            (" * This is an unordered list", "unordered_list"),
            ("- This is an unordered list", "unordered_list"),
            (" *This is not an unordered list", "paragraph"),
            ("-This is not an unordered list", "paragraph"),


            ("1. This is an ordered list", "ordered_list"),
            (" 233. This is an ordered list", "ordered_list"),
            ("1 This is not an ordered list", "paragraph"),
            ("1This is not an ordered list", "paragraph"),
            ("1.This is not an ordered list", "paragraph")
        ]

        for text, expected in test_cases: 
            with self.subTest(text = text, expected = expected):
                result = block_to_block_type(text) 
                self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()