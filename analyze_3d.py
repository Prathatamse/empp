import re

content = open('index.html', encoding='utf-8').read()

# The 3D may use Three.js - look for relevant patterns
# Check what happens near the canvas elements
canvas_positions = [m.start() for m in re.finditer(r'<canvas', content)]
print(f"Canvas elements: {len(canvas_positions)}")
for pos in canvas_positions:
    snippet = content[pos:pos+300]
    print(f"\n--- canvas at {pos} ---")
    print(snippet[:200])

# Also look for wordGap or related props in scripts
for keyword in ['wordGap', 'word_gap', 'letterSpacing', 'letter-spacing', 'spacing', 'gap']:
    found = [(m.start(), content[max(0,m.start()-50):m.start()+100]) for m in re.finditer(keyword, content)]
    if found:
        print(f"\n=== {keyword} ({len(found)} hits) ===")
        for pos, snip in found[:3]:
            print(f"  pos={pos}: {snip[:100]}")
