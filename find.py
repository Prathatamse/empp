import json
with open('index.html', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if 'module' in line and '<script' in line:
            print(f"{i+1}: {line[:200]}")
