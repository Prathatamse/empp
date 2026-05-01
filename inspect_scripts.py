import re

content = open('index.html', encoding='utf-8').read()

# The 3D canvas is in framer-ljc3kb-container
# It's a custom Framer plugin - let's see the script tags content

# Find all script tags and look inside them
script_pattern = re.compile(r'<script([^>]*)>(.*?)</script>', re.DOTALL)
scripts = list(script_pattern.finditer(content))
print(f"Total scripts: {len(scripts)}")

for i, s in enumerate(scripts):
    attrs = s.group(1)
    body = s.group(2)
    if len(body) > 50:
        print(f"\nScript {i+1}: attrs={attrs[:100]}, body len={len(body)}")
        # Look for 3D-related code
        if any(kw in body for kw in ['canvas', 'Canvas', 'rotate', 'Rotate', '3d', 'ring', 'Ring', 'Home', 'Contact']):
            print("  ** Contains relevant keywords **")
            # Find nav item array
            navmatch = re.search(r'(\[.*?(?:Home|Contact|Cases|Presence).*?\])', body)
            if navmatch:
                print(f"  Nav array: {navmatch.group(0)[:200]}")
            else:
                print(f"  Body preview: {body[:200]}")
