import re

content = open('index.html', encoding='utf-8').read()

# Get full context around each canvas
canvas_positions = [m.start() for m in re.finditer(r'<canvas', content)]

output = []
for i, pos in enumerate(canvas_positions):
    # Go back 2000 chars to find the script containing this canvas
    start = max(0, pos - 3000)
    end = min(len(content), pos + 500)
    snippet = content[start:end]
    output.append(f"=== CANVAS {i+1} at pos {pos} ===\n{snippet}\n")

open('out_canvas_ctx.txt', 'w', encoding='utf-8').write('\n'.join(output))
print(f"Wrote {len(canvas_positions)} canvas contexts")
