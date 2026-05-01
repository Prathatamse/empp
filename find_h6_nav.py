import re

content = open('index.html', encoding='utf-8').read()

# Find all the h6 nav-3d items - they have framer-styles-preset-753q9u
# These are directly: Home, Contact, Cases, Presence, Services
# Find exact pattern of those h6 tags
pattern = re.compile(
    r'(<h6 class="framer-text framer-styles-preset-753q9u"[^>]*>)'
    r'\s*(Home|Contact|Cases|Presence|Services)'
    r'(<span class="nav-3d-spacer"[^>]*>.*?</span>)</h6>',
    re.DOTALL
)

matches = list(pattern.finditer(content))
print(f"Found {len(matches)} nav h6 items")
for m in matches:
    print(f"  [{m.group(2)}] at offset {m.start()}")
    print(f"  Full: {m.group(0)[:200]}")
    print()
