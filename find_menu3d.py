import urllib.request
import re
import concurrent.futures

with open('e:/New folder/website-export/index.html', encoding='utf-8') as f:
    html = f.read()

urls = list(set(re.findall(r'https://framerusercontent.com[^\s\"\'<>]*?\.mjs', html)))

print(f"Found {len(urls)} remote .mjs URLs to scan...")

def check(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        txt = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        if 'curveRadius' in txt and 'gapPx' in txt: 
            return url
    except Exception as e: 
        pass
    return None

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for res in executor.map(check, urls):
        if res: 
            print('FOUND:', res)
