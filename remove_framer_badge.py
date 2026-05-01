import os
import re

css_fix = '<style>.framer-1vgnsuv, a[href*="framer.com/"] { display: none !important; opacity: 0 !important; pointer-events: none !important; }</style>'

def fix_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Search for exactly where we can append the CSS
    if css_fix in content:
        return False
        
    new_content = content.replace('</body>', css_fix + '\n</body>')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

changed = 0
for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.html'):
            filepath = os.path.join(root, filename)
            if fix_html(filepath):
                changed += 1
                
print(f'Applied CSS fix to {changed} HTML files.')
