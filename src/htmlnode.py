class HtmlNode: 
    def __init__(self, tag: str = None, value: str = None, children: list['HtmlNode'] = None, props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children 
        self.props = props 

    def to_html(self): 
        result =  f"<{self.tag}"
        if self.props: 
            result += self.props_to_html()
        result += ">"

        if self.children: 
            for child in self.children: 
                result += str(child)
        else: 
            result += self.value
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
     
