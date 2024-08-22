class HtmlNode: 
    def __init__(self, tag: str = None, value: str = None, children: list['HtmlNode'] = None, props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self): 
        result =  f"<{self.tag}"
        result += self.props_to_html()
        result += ">"

        if len(self.children) > 0: 
            for child in self.children: 
                result += str(child)
        else: 
            result += self.value
        result += f"</{self.tag}>"
        return result
    
    def props_to_html(self): 
        html = ""
        for key, value in self.props.items(): 
            html += f" {key}='{value}'"
        return html
    
    def __repr__(self) -> str:
        return self.to_html()