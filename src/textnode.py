from htmlnode import HtmlNode
from leafnode import LeafNode
#from markdown_blocks import markdown_to_blocks
import re

class TextNode: 
    TEXT_TYPE_TEXT = "text"
    TEXT_TYPE_BOLD = "bold"
    TEXT_TYPE_ITALIC = "italic"
    TEXT_TYPE_CODE = "code"
    TEXT_TYPE_LINK = "link"
    TEXT_TYPE_IMAGE = "image"

    def __init__(self, text, text_type, url = None): 
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(node1, node2): 
        return node1.text == node2.text \
          and node1.text_type == node2.text_type \
          and node1.url == node2.url

    def __repr__(self):
        return F"TextNode({self.text}, {self.text_type}, {self.url})" 
    
    def text_node_to_html_node(text_node): 
        if not text_node or not text_node.text_type: 
            raise Exception("invalid text node")
        match text_node.text_type: 
            case TextNode.TEXT_TYPE_TEXT: 
                return LeafNode(value=text_node.text)
            case TextNode.TEXT_TYPE_BOLD: 
                return LeafNode(value=text_node.text, tag="b")
            case TextNode.TEXT_TYPE_ITALIC: 
                return LeafNode(value=text_node.text, tag="i")
            case TextNode.TEXT_TYPE_CODE: 
                return LeafNode(value=text_node.text, tag="code")
            case TextNode.TEXT_TYPE_LINK: 
                props = {"href": text_node.url}
                return LeafNode(tag="a", value=text_node.text, props=props)
            case TextNode.TEXT_TYPE_IMAGE: 
                props = {"src": text_node.url, "alt": text_node.text}
                return LeafNode(value="", tag="img", props = props)
            case _: 
                raise Exception(f"Invalid text type: {text_node.text_type}")



    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        main_type = TextNode.TEXT_TYPE_TEXT
        delimited_type = text_type
        for old_node in old_nodes: 
            if old_node.text_type != TextNode.TEXT_TYPE_TEXT:
                new_nodes.append(old_node)
                continue
            fields = old_node.text.split(delimiter)
            isDelimited = old_node.text[0] == delimiter[0]
            for field in fields: 
                if field == '': 
                    continue
                new_nodes.append(TextNode(field, delimited_type if isDelimited else main_type))
                isDelimited = not isDelimited
            
        return new_nodes

    def get_link_text(text: str, href: str) -> str: 
        # [to boot dev](https://www.boot.dev)
        return f"[{text}]({href})"

    def get_image_text(text: str, href: str) -> str: 
        # ![rick roll](https://i.imgur.com/aKaOqIh.gif)
        return f"![{text}]({href})"

    def split_nodes_image(old_nodes):
        new_nodes = []
        for node in old_nodes: 
            images = TextNode.extract_markdown_images(node.text)
            if images == []: 
                new_nodes.append(node)
                continue
            i1 = 0
            i2 = 0
            for image in images: 
                imageText = TextNode.get_image_text(*image)
                i2 = node.text.index(imageText, i1)
                if i2 == -1: 
                    raise Exception(f"image not found but it should be, man. Image: {imageText}. NodeText: {node.text}")
                if i2 > i1: 
                    new_nodes.append(TextNode(node.text[i1:i2], TextNode.TEXT_TYPE_TEXT))
                    i1 = i2
                i2 += len(imageText)
                new_nodes.append(TextNode(image[0], TextNode.TEXT_TYPE_IMAGE, image[1]))
                i1 = i2  
            if i2 < len(node.text) - 1: 
                new_nodes.append(TextNode(node.text[i2:], TextNode.TEXT_TYPE_TEXT))                          
        return new_nodes

    def split_nodes_link(old_nodes : list['TextNode']) -> list['TextNode']:
        new_nodes = []
        for node in old_nodes: 
            links = TextNode.extract_markdown_links(node.text)
            if links == []: 
                new_nodes.append(node)
                continue
            i1 = 0
            i2 = 0
            for link in links: 
                linkText = TextNode.get_link_text(*link)
                i2 = node.text.index(linkText, i1)
                if i2 == -1: 
                    raise Exception(f"image not found but it should be, man. Image: {linkText}. NodeText: {node.text}")
                if i2 > i1: 
                    new_nodes.append(TextNode(node.text[i1:i2], TextNode.TEXT_TYPE_TEXT))
                    i1 = i2
                i2 += len(linkText)
                new_nodes.append(TextNode(link[0], TextNode.TEXT_TYPE_LINK, link[1]))
                i1 = i2  
            if i2 < len(node.text) - 1: 
                new_nodes.append(TextNode(node.text[i2:], TextNode.TEXT_TYPE_TEXT))                          
        return new_nodes

    def extract_markdown_images(text:str): 
        images = [] 
         #  ![rick roll](https://i.imgur.com/aKaOqIh.gif)
        pattern = r"!\[(.*?)\]\((.*?)\)"
        matches = re.findall(pattern, text)
        for match in matches: 
            images.append((match[0], match[1]))

        return images


    def extract_markdown_links(text : str) -> list[str]: 
        links = []
        #  [to boot dev](https://www.boot.dev)
        pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
        matches = re.findall(pattern, text)
        for match in matches: 
            links.append((match[0], match[1]))
        return links
    
    def text_to_textnodes(text: str) -> list['TextNode']:
        workingText = text
        nodes = [] 
        while len(workingText) > 0: 
            next_node_type = TextNode.__get_next_node_type(workingText)
            next_nodes = []
            old_nodes = [TextNode(workingText, TextNode.TEXT_TYPE_TEXT)]
            match next_node_type: 
                case TextNode.TEXT_TYPE_TEXT: 
                    next_nodes.extend(old_nodes)
                case TextNode.TEXT_TYPE_BOLD:
                    next_nodes =  TextNode.split_nodes_delimiter(old_nodes, "**", next_node_type)
                case TextNode.TEXT_TYPE_ITALIC:
                    next_nodes =  TextNode.split_nodes_delimiter(old_nodes, "*", next_node_type)
                case TextNode.TEXT_TYPE_CODE:
                    next_nodes =  TextNode.split_nodes_delimiter(old_nodes, "`", next_node_type)
                case TextNode.TEXT_TYPE_LINK:
                    next_nodes =  TextNode.split_nodes_link(old_nodes)
                case TextNode.TEXT_TYPE_IMAGE:
                    next_nodes =  TextNode.split_nodes_image(old_nodes)

            for j in range(len(next_nodes) - 1): 
                nodes.append(next_nodes[j])
            if next_nodes[-1].text_type == TextNode.TEXT_TYPE_TEXT: 
                workingText = next_nodes[-1].text
            else: 
                nodes.append(next_nodes[-1])
                workingText = ""

        return nodes    


    #def block_to_block_type(block: str) -> str: 
        """
        paragraph
        heading
        code
        quote
        unordered_list
        ordered_list

        Headings start with 1-6 # characters, followed by a space and then the heading text.
        Code blocks must start with 3 backticks and end with 3 backticks.
        Every line in a quote block must start with a > character.
        Every line in an unordered list block must start with a * or - character, followed by a space.
        Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
        If none of the above conditions are met, the block is a normal paragraph.

        """

        """
        pattern = "^\s*[#]{1,6}\s"
        if re.match(pattern, block): 
            return "heading"
        
        pattern = "^\s*```(.*?)```$"
        if re.match(pattern, block): 
            return "code"

        pattern = "^\s*>(.*?)$"
        if re.match(pattern, block): 
            return "quote"

        pattern = "^\s*[-|\*]+\s"
        if re.match(pattern, block):
            return "unordered_list"
        
        pattern = "^\s*\d+\.\s(.*?)"
        if re.match(pattern, block):
            return "ordered_list"

        return "paragraph" 
    """

    def __get_next_node_type(text: str) -> str: 
        i = 0 
        result = TextNode.TEXT_TYPE_TEXT
        print(f"Testing {text}")
        while i < len(text): 
            match text[i]: 
                case '*': 
                    if i < len(text) - 1 and text[i + 1] == '*': 
                        if text.find("**", i + 2) > -1: 
                            result = TextNode.TEXT_TYPE_BOLD
                    else:
                        if text.find("*", i + 1) > -1: 
                            result = TextNode.TEXT_TYPE_ITALIC
                case '`': 
                    if text.find("`", i + 1) > -1: 
                        result = TextNode.TEXT_TYPE_CODE
                case '!': 
                    if i < len(text) - 1 and text[i + 1] == '[': 
                        j = text.find(']', i + 2)
                        if (j > -1 and j < len(text) - 1 and text[j + 1] == '('): 
                            j = text.find(')', j + 2)
                            if j > -1: 
                                result = TextNode.TEXT_TYPE_IMAGE
                case '[': 
                    j = text.find(']', i + 1)
                    if (j > -1 and j < len(text) - 1 and text[j + 1] == '('): 
                        j = text.find(')', j + 2)
                        if j > -1: 
                            result = TextNode.TEXT_TYPE_LINK
            if result != TextNode.TEXT_TYPE_TEXT: 
                break
            i += 1
        return result

                        
    def text_to_children(block : str) -> 'HtmlNode': 
        text_nodes = TextNode.text_to_textnodes(block)
        children = []
        for text_node in text_nodes:
            html_node = TextNode.text_node_to_html_node(text_node)
            children.append(html_node)
        return children

    """
    def markdown_to_html(markdown : str) -> 'HtmlNode': 
        blocks = markdown_to_blocks(markdown)
        html_nodes = []
        for block in blocks: 
            html_nodes.append(TextNode.text_to_children(block))
        
        wrapper = HtmlNode(tag="div", children=html_nodes)
        return wrapper                    
    """

