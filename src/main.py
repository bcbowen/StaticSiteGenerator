import os
import re
import shutil
from pathlib import Path
from textnode import TextNode
from htmlnode import HtmlNode

def remove_contents(dest : str): 
    for root, dirs, files in os.walk(dest, topdown=False): 
        for file in files: 
            os.remove(Path(root) / file) # remove files
        
        for dir in dirs: 
            os.rmdir(Path(root) / dir) # remove empty directories

def copy_contents(src: str, dest: str): 
    for root, dirs, files in os.walk(src): 
        relative_path = os.path.relpath(root, src)
        dest_dir = Path(dest) / relative_path
        if not dest_dir.exists(): 
            os.mkdir(dest_dir)

        for file in files: 
            src_file = Path(root) / file
            dest_file = dest_dir / file
            shutil.copy2(src_file, dest_file)

def copy_directory(src: str, dest: str): 
    remove_contents(dest)
    copy_contents(src, dest)

def extract_title(markdown): 
    lines = markdown.split('\n')
    pattern = r"^\s*#{1}\s(.*)"
    for line in lines: 
        match = re.match(pattern, line)
        if match: 
            return match.group(1).strip()
    raise Exception("h1 not found")

def generate_page(from_path, template_path, dest_path): 
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file_text = "" 
    template_text = ""

    print(os.getcwd()) 

    with open(from_path) as file: 
        file_text = file.read()
        file.close() 
    
    with open(template_path) as template: 
        template_text = template.read()
        template.close()

    html = TextNode.markdown_to_html(file_text)
    html_text = HtmlNode.to_html(html)
    
    title = extract_title(file_text)

    template_text = template_text.replace("{{ Title }}", title)
    template_text = template_text.replace("{{ Content }}", html_text)

    dest_dir = Path(dest_path).parent
    os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as new_file: 
        new_file.write(template_text)
        new_file.close()
    


def main(): 
    copy_directory("static", "public")

    base_path = Path(__file__).parents[1]
    #print(f"base path: {base_path}")
    from_path = os.path.join(base_path, 'content/index.md')
    template_path = os.path.join(base_path, 'src/template.html')
    dest_path = os.path.join(base_path, "public/index.html")
    generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
    main() 