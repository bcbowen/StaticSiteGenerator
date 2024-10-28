from htmlnode import HtmlNode

class ParentNode(HtmlNode): 
    def __init__(self, tag: str, children: list['HtmlNode'], props: dict[str, str] = None):
        super().__init__(children = children, tag = tag, props = props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self): 
        result = ""
        if self.tag == None: 
            raise ValueError('Tag is required')
        if self.children == None or len(self.children) == 0: 
            raise ValueError('Parent node needs children')
        
        result = f"<{self.tag}"
        if self.props: 
            result += self.props_to_html()
        result += ">"
        for child in self.children: 
            result += child.to_html()
        result += f"</{self.tag}>"
        
        return result
        
    
    def props_to_html(self): 
        html = ""
        if self.props: 
            for key, value in self.props.items(): 
                html += f" {key}='{value}'"
        return html
    
    def __repr__(self) -> str:
        return self.to_html()