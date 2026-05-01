import re, json

content = open('index.html', encoding='utf-8').read()

# The 3D ring is a Framer component. Framer serializes component props as JSON 
# inside script tags, typically as window.__framer_importFromPackage or similar
# Look for JSON blobs containing the nav item text pattern
# The key is wordGap or similar
for keyword in ['wordGap', 'word_gap', 'wordSpacing', 'word-spacing', 'itemGap', 'itemSpacing']:
    idx = content.find(keyword)
    if idx != -1:
        print(f"FOUND: {keyword} at {idx}")
        print(content[max(0, idx-100):idx+300])
    else:
        print(f"NOT FOUND: {keyword}")

# Also look at the data-font-key container - that div controls the 3D canvas
# Find its script initialization
idx = content.find('data-font-key')
print(f"\nFirst data-font-key at {idx}")
print(content[max(0, idx-300):idx+300])
