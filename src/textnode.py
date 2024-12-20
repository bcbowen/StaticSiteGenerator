from htmlnode import HtmlNode
from leafnode import LeafNode
from text_type import TextType
import re

class TextNode: 

    def __init__(self, text : str, text_type : TextType, url = None): 
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(node1 : TextType, node2 : TextType) -> bool: 
        return node1.text == node2.text \
          and node1.text_type == node2.text_type \
          and node1.url == node2.url

    def __repr__(self):
        return F"TextNode({self.text}, {self.text_type.value}, {self.url})" 
    
    def text_node_to_html_node(text_node : 'TextNode') -> HtmlNode: 
        if not text_node or not text_node.text_type: 
            raise Exception("invalid text node")
        match text_node.text_type: 
            case TextType.TEXT: 
                return LeafNode(value=text_node.text)
            case TextType.BOLD: 
                return LeafNode(value=text_node.text, tag="b")
            case TextType.ITALIC: 
                return LeafNode(value=text_node.text, tag="i")
            case TextType.CODE: 
                return LeafNode(value=text_node.text, tag="code")
            case TextType.LINK: 
                props = {"href": text_node.url}
                return LeafNode(tag="a", value=text_node.text, props=props)
            case TextType.IMAGE: 
                props = {"src": text_node.url, "alt": text_node.text}
                return LeafNode(value="", tag="img", props = props)
            case _: 
                raise Exception(f"Invalid text type: {text_node.text_type}")


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
                    new_nodes.append(TextNode(node.text[i1:i2], TextType.TEXT))
                    i1 = i2
                i2 += len(imageText)
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                i1 = i2  
            if i2 < len(node.text) - 1: 
                new_nodes.append(TextNode(node.text[i2:], TextType.TEXT))                          
        return new_nodes
    
    def extract_markdown_links(text : str) -> list[str]:
        pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
        matches = re.findall(pattern, text)
        return matches
    
    def split_nodes_link(old_nodes: list['TextNode']) -> list['TextNode']:
        new_nodes = []
        for old_node in old_nodes:
            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue
            original_text = old_node.text
            links = TextNode.extract_markdown_links(original_text)
            if len(links) == 0:
                new_nodes.append(old_node)
                continue
            for link in links:
                sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, link section not closed")
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
        return new_nodes

    def extract_markdown_images(text : str) -> list[str]:
        pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        matches = re.findall(pattern, text)
        return matches
    
    
    def split_nodes_delimiter(old_nodes : list['TextNode'], delimiter : str, text_type: TextType) -> list['TextNode']:
        new_nodes = []
        for old_node in old_nodes:
            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue
            split_nodes = []
            sections = old_node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise ValueError("Invalid markdown, formatted section not closed")
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(sections[i], text_type))
            new_nodes.extend(split_nodes)
        return new_nodes
    
    
    def text_to_textnodes(text : str) -> list['TextNode']:
        nodes = [TextNode(text, TextType.TEXT)]
        nodes = TextNode.split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = TextNode.split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        nodes = TextNode.split_nodes_delimiter(nodes, "`", TextType.CODE)
        nodes = TextNode.split_nodes_image(nodes)
        nodes = TextNode.split_nodes_link(nodes)
        return nodes 

    def text_to_children(block : str) -> 'HtmlNode': 
        text_nodes = TextNode.text_to_textnodes(block)
        children = []
        for text_node in text_nodes:
            html_node = TextNode.text_node_to_html_node(text_node)
            children.append(html_node)
        return children


