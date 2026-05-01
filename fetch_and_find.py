import urllib.request
import re
import os
import concurrent.futures

os.makedirs('fjs', exist_ok=True)

with open('index.html', encoding='utf-8') as f:
    html = f.read()

urls = list(set(re.findall(r'https://framerusercontent.com[^\s\"\'<>]*?\.mjs', html)))
print(f"Downloading {len(urls)} files to ./fjs/ ...")

def download(url):
    fname = os.path.basename(url)
    out_path = os.path.join('fjs', fname)
    if os.path.exists(out_path): 
        return url
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5).read()
        with open(out_path, 'wb') as out:
            out.write(res)
        return url
    except Exception as e:
        print(f"Failed {fname}: {e}")
        return None

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for res in executor.map(download, urls):
        pass

print("Done downloading.")
