import re

content = open('index.html', encoding='utf-8').read()

# Search for all script tags containing canvas or 3D drawing code
# Look for where the nav items are constructed as JS strings/arrays
idx = 0
found = []
while True:
    idx = content.find('"Contact"', idx)
    if idx == -1:
        break
    found.append(idx)
    idx += 1

print(f"Found 'Contact' as JS string at {len(found)} places")
for pos in found:
    snippet = content[max(0,pos-100):pos+200]
    open(f'out_js_contact_{pos}.txt', 'w', encoding='utf-8').write(snippet)
    print(f"  Pos {pos}: {snippet[:80].strip()}")
