import re

with open(r'e:\New folder\website-export\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = [m.start() for m in re.finditer(r'>Services<', content)]
for m in matches:
    start = max(0, m - 500)
    end = min(len(content), m + 500)
    print("--- MATCH ---")
    print(content[start:end])
    print("\n\n")
