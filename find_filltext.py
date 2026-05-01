import re

content = open('index.html', encoding='utf-8').read()

# Look at the 3D component - look for script drawing code
# The 3D ring likely uses a Framer component that reads from children
# Look for "fillText" (canvas 2D API) which is used to draw text
matches = [(m.start(), content[max(0,m.start()-200):m.start()+400]) for m in re.finditer(r'fillText', content)]
print(f"fillText references: {len(matches)}")
for pos, snippet in matches[:5]:
    print(f"\n--- pos {pos} ---")
    print(snippet[:300])

results = '\n\n'.join(f"pos={pos}\n{snippet}" for pos,snippet in matches)
open('out_filltext.txt', 'w', encoding='utf-8').write(results)
