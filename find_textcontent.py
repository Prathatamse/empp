import re

content = open('index.html', encoding='utf-8').read()

# Find 3D component JS - look for canvas/three.js patterns
# The component likely reads innerText from the DOM
# Search for "innerText" or "textContent" usage near nav
matches_innerText = [(m.start(), content[max(0,m.start()-100):m.start()+200]) for m in re.finditer(r'innerText|textContent', content)]
print(f"innerText/textContent references: {len(matches_innerText)}")
for pos, snippet in matches_innerText[:10]:
    print(f"\n--- pos {pos} ---")
    print(snippet[:200])

results = '\n\n'.join(f"pos={pos}\n{snippet}" for pos,snippet in matches_innerText)
open('out_innertext.txt', 'w', encoding='utf-8').write(results)
