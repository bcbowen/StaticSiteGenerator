from htmlnode import HtmlNode

class LeafNode(HtmlNode): 
    def __init__(self, value: str, tag: str = None, props: dict[str, str] = None):
        super().__init__(value = value, tag = tag, props = props, children = None)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self): 
        result = ""
        if self.tag == None: 
            result = self.value
        else: 
            result = f"<{self.tag}"
            if self.props: 
                result += self.props_to_html()
            result += ">"
            result += self.value
            result += f"</{self.tag}>"
        
        return result
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, LeafNode): 
            return False
        return self.value  == value.value and \
            self.children == value.children and \
            self.props == value.props and \
            self.tag == value.tag
    
    def props_to_html(self): 
        html = ""
        if self.props: 
            for key, value in self.props.items(): 
                html += f" {key}='{value}'"
        return html
    
    def __repr__(self) -> str:
        return self.to_html()