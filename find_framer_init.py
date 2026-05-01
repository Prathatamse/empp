import re

content = open('index.html', encoding='utf-8').read()

# Look in the big JS bundle section - find all script tags
script_matches = list(re.finditer(r'<script[^>]*>(.*?)</script>', content, re.DOTALL))
print(f"Total script tags: {len(script_matches)}")

# Also look for framer-component initialization that might pass props
# The 3D ring menu is likely a Framer component that gets props via React hydration
# Look for the nav items in __NEXT_DATA__ or similar
for keyword in ['__NEXT_DATA__', '__framerProps', 'Contact\\\\n', 'ContactHome', 'Presence\\n']:
    idx = content.find(keyword)
    if idx != -1:
        print(f"FOUND: {keyword} at {idx}")
    else:
        print(f"NOT FOUND: {keyword}")

# Look for the framer-component container with the nav items
# Search for h6 tags containing the nav labels
h6_matches = list(re.finditer(r'<h6[^>]*?framer-styles-preset-753q9u[^>]*?>.*?</h6>', content, re.DOTALL))
print(f"\nFound {len(h6_matches)} h6 with framer-styles-preset-753q9u")
for m in h6_matches[:5]:
    print(f"  -> {m.group(0)[:200]}")
