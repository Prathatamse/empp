import re
import json

with open(r'e:\New folder\website-export\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

classes_to_find = [
    'framer-tppbh', 'framer-17go8qu', 'framer-jky3ly', 'framer-1743wqy-container',
    'framer-4Nae1', 'framer-72rtr7', 'framer-1x3tzhw-container', 'framer-BDvJp',
    'framer-FbrZO', 'framer-5ed1i1', 'framer-40t19v', 'framer-12e8q36'
]

results = {}
for cls in classes_to_find:
    pattern = re.compile(r'(\.[a-zA-Z0-9_\-\s>]*' + re.escape(cls) + r'[a-zA-Z0-9_\-\s>]*\{[^}]+\})')
    matches = pattern.findall(content)
    if matches:
        results[cls] = matches
    
    # also search media queries containing this class
    mq_pattern = re.compile(r'(@media[^\{]+\{\s*(?:\.[^{}]+\{[^}]+\}\s*)*\.[a-zA-Z0-9_\-\s>]*' + re.escape(cls) + r'[a-zA-Z0-9_\-\s>]*\{[^}]+\}(?:\s*\.[^{}]+\{[^}]+\})*\s*\})')
    # This might be tricky to regex reliably, so let's stick to the basic classes first

with open('css_output.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
