from htmlnode import HtmlNode

class ParentNode(HtmlNode): 
    def __init__(self, children: list['HtmlNode'] = None, tag: str = None, props: dict[str, str] = None):
        super().__init__(children = children, tag = tag, props = props)
        self.tag = tag
        self.children = children
        self.props = props if props is not None else {}

    def to_html(self): 
        result = ""
        if self.tag == None: 
            raise ValueError('Tag is required')
        if self.children == None or len(self.children) == 0: 
            raise ValueError('Parent node needs children')
        
        result = f"<{self.tag}"
        result += self.props_to_html()
        result += ">"
        for child in self.children: 
            result += child.to_html()
        result += f"</{self.tag}>"
        
        return result
        
    
    def props_to_html(self): 
        html = ""
        for key, value in self.props.items(): 
            html += f" {key}='{value}'"
        return html
    
    def __repr__(self) -> str:
        return self.to_html()