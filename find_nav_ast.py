from html.parser import HTMLParser

class NavParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.found = False
    
    def handle_starttag(self, tag, attrs):
        if not self.found:
            self.tags.append((tag, dict(attrs)))
        
    def handle_endtag(self, tag):
        if not self.found and self.tags:
            # Note: this is a simple parser, might not handle void elements perfectly
            # but usually fine to get the path
            if self.tags[-1][0] == tag:
                 self.tags.pop()
            else:
                 # find the last matching tag and pop up to it
                 for i in range(len(self.tags)-1, -1, -1):
                     if self.tags[i][0] == tag:
                         self.tags = self.tags[:i]
                         break
            
    def handle_data(self, data):
        if 'Services' in data and not self.found:
            self.found = True
            print(f"Found '{data.strip()}'!")
            print("Hierarchy:")
            for t, a in self.tags[-8:]:
                class_attr = a.get('class', '')
                id_attr = a.get('id', '')
                style_attr = a.get('style', '')
                name_attr = a.get('name', '')
                print(f"<{t} class='{class_attr}' id='{id_attr}' style='{style_attr}' name='{name_attr}'>")

parser = NavParser()
with open(r'e:\New folder\website-export\index.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())
