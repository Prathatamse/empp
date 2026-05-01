import re

content = open('index.html', encoding='utf-8').read()

# Find all h6 with framer-styles-preset-753q9u and their parents to understand context
# These are the 3D ring nav items
pattern = re.compile(r'<h6 class="framer-text framer-styles-preset-753q9u".*?</h6>', re.DOTALL)
matches = list(pattern.finditer(content))
print(f"Found {len(matches)} matching h6 elements")
for i, m in enumerate(matches):
    text = m.group(0)
    # Get some context before to see what container this is in
    before = content[max(0, m.start()-300):m.start()]
    # Find the last data-framer-name in before
    names = re.findall(r'data-framer-name="([^"]+)"', before)
    print(f"\nH6 #{i+1}:")
    print(f"  Text content: {text[text.find('>')+1:text.find('>')+50]}")
    print(f"  Parent context: {names[-3:] if names else 'unknown'}")
    print(f"  Full tag: {text[:200]}")
