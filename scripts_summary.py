import re

content = open('index.html', encoding='utf-8').read()

script_pattern = re.compile(r'<script([^>]*)>(.*?)</script>', re.DOTALL)
scripts = list(script_pattern.finditer(content))

output = []
for i, s in enumerate(scripts):
    attrs = s.group(1)
    body = s.group(2)
    if len(body) > 50:
        output.append(f"=== Script {i+1} (len {len(body)}) attrs: {attrs[:80]} ===")
        output.append(body[:500])
        output.append("")

open('out_scripts_summary.txt', 'w', encoding='utf-8').write('\n'.join(output))
print(f"Done - {len(scripts)} scripts")
