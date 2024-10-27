import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from textnode import TextNode
from markdown_blocks import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_markdown_to_html_simple_paragraph(self): 
        block = "This is a paragraph"
        html = markdown_to_html_node(block)
        self.assertEqual(html.tag, "div")
        self.assertEqual(len(html.children), 1)
        self.assertEqual(html.children[0].tag, "p")
        self.assertEqual(html.children[0].children[0].value, block)

    def test_markdown_to_html_simpleH1(self):
        value = "This is a H1"
        block = f"# {value}"
        html = markdown_to_html_node(block)
        self.assertEqual(html.tag, "div")
        self.assertEqual(len(html.children), 1)
        self.assertEqual(html.children[0].tag, "h1")
        self.assertEqual(html.children[0].children[0].value, value)

    def test_markdown_to_html_simpleH2(self):
        value = "This is a H2"
        block = f"## {value}"
        html = markdown_to_html_node(block)
        self.assertEqual(html.tag, "div")
        self.assertEqual(len(html.children), 1)
        self.assertEqual(html.children[0].tag, "h2")
        self.assertEqual(html.children[0].children[0].value, value)   

    def test_markdown_to_html_simpleH3(self):
        value = "This is a H3"
        block = f"### {value}"
        html = markdown_to_html_node(block)
        self.assertEqual(html.tag, "div")
        self.assertEqual(len(html.children), 1)
        self.assertEqual(html.children[0].tag, "h3")
        self.assertEqual(html.children[0].children[0].value, value)       

    def test_markdown_to_html_simpleH6(self):
        value = "This is a H6"
        block = f"###### {value}"
        html = markdown_to_html_node(block)
        self.assertEqual(html.tag, "div")
        self.assertEqual(len(html.children), 1)
        self.assertEqual(html.children[0].tag, "h6")
        self.assertEqual(html.children[0].children[0].value, value)          

    def test_markdown_to_html_simple_code(self):
        value = "10 goto 10"
        block = f"```{value}```"
        html = markdown_to_html_node(block)
        self.assertEqual(html.tag, "div")
        self.assertEqual(len(html.children), 1)
        self.assertEqual(html.children[0].tag, "pre")
        pre = html.children[0]
        self.assertEqual(len(pre.children), 1)
        self.assertEqual(pre.children[0].tag, "code")
        self.assertEqual(pre.children[0].children[0].value, value) 

    def test_markdown_to_html_simple_quote(self):
        block = """> First of all, you're fired!
> Yeah, I kinda figured that, Glenn"""
        html = markdown_to_html_node(block)
        self.assertEqual(html.tag, "div")
        self.assertEqual(len(html.children), 1)
        self.assertEqual(html.children[0].tag, "blockquote")
        quote = html.children[0]
        lines = quote.value.split('\n')
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], "First of all, you're fired!")
        self.assertEqual(lines[1], "Yeah, I kinda figured that, Glenn")
    
    def test_markdown_to_html_simple_unordered_list(self):
        block = """* dental floss
* grappeling hook"""
        html = markdown_to_html_node(block)
        self.assertEqual(html.tag, "div")
        self.assertEqual(len(html.children), 1)
        self.assertEqual(html.children[0].tag, "ul")
        ul = html.children[0]
        self.assertEqual(len(ul.children), 2)
        self.assertEqual(ul.children[0].tag, "li")
        self.assertEqual(ul.children[0].value, "dental floss")
        self.assertEqual(ul.children[1].tag, "li")
        self.assertEqual(ul.children[1].value, "grappeling hook")

    def test_markdown_to_html_simple_ordered_list(self):
        block = """1. steal socks 
2. profit"""
        html = markdown_to_html_node(block)
        self.assertEqual(html.tag, "div")
        self.assertEqual(len(html.children), 1)
        self.assertEqual(html.children[0].tag, "ol")
        ul = html.children[0]
        self.assertEqual(len(ul.children), 2)
        self.assertEqual(ul.children[0].tag, "li")
        self.assertEqual(ul.children[0].value, "steal socks")
        self.assertEqual(ul.children[1].tag, "li")
        self.assertEqual(ul.children[1].value, "profit")

    def test_markdown_to_html_big_shebang(self): 
        markdown = """# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn\'t work yet)
All that is gold does not glitter
## Reasons I like Tolkien"

* You can spend years studying the legendarium and still not understand its depths
* It can be enjoyed by children and adults alike
* Disney *didn't ruin it*
* It created an entirely new genre of fantasy
## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn
Here's what `elflang` looks like (the perfect coding language):
```
    func main(){
        fmt.Println(\"Hello, World!\")
    }
```"""
        html = markdown_to_html_node(markdown)
        self.assertEqual(html.tag, "div")
        self.assertEqual(html.children[0].tag, "h1")


if __name__ == "__main__":
    unittest.main()