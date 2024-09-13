from leafnode import LeafNode
import re

class TextNode: 
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
            case "text": 
                return LeafNode(value=text_node.text)
            case "bold": 
                return LeafNode(value=text_node.text, tag="b")
            case "italic": 
                return LeafNode(value=text_node.text, tag="i")
            case "code": 
                return LeafNode(value=text_node.text, tag="code")
            case "link": 
                props = {"href": text_node.url}
                return LeafNode(tag="a", value=text_node.text, props=props)
            case "image": 
                props = {"src": text_node.url, "alt": text_node.text}
                return LeafNode(value="", tag="img", props = props)
            case _: 
                raise Exception(f"Invalid text type: {text_node.text_type}")



    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        main_type = "text"
        delimited_type = text_type
        for old_node in old_nodes: 
            if old_node.text_type != "text":
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

    def extract_markdown_images(text): 
        images = [] 
         #  ![rick roll](https://i.imgur.com/aKaOqIh.gif)
        pattern = r"!\[(.*?)\]\((.*?)\)"
        matches = re.findall(pattern, text)
        for match in matches: 
            images.append((match[0], match[1]))

        return images


    def extract_markdown_links(text): 
        links = []
        #  [to boot dev](https://www.boot.dev)
        pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
        matches = re.findall(pattern, text)
        for match in matches: 
            links.append((match[0], match[1]))
        return links
             
