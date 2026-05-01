from bs4 import BeautifulSoup
import re

with open(r'e:\New folder\website-export\index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

services_elems = soup.find_all(string=re.compile("Services"))
with open("output.txt", "w", encoding="utf-8") as out:
    for elem in services_elems:
        out.write(f"Text: {elem.strip()}\n")
        parent = elem.parent
        out.write("Hierarchy:\n")
        for _ in range(8):
            if parent:
                out.write(f"<{parent.name} class='{parent.get('class')}'>\n")
                parent = parent.parent
        out.write("-----\n")
