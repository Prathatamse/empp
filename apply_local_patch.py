import re
import os

target_files = ['script_main.zMWyeqfe.mjs', 'script_main.D_QN_HoU.mjs']
export_dir = 'e:/New folder/website-export'
fjs_dir = os.path.join(export_dir, 'fjs')

for fname in target_files:
    fpath = os.path.join(fjs_dir, fname)
    if not os.path.exists(fpath): continue
    
    js = open(fpath, encoding='utf-8').read()
    
    # We find the minified `layout()` function which starts with `function m(){let e=j.current.uBend.value...`
    # Since variable names might be different, we use a regex to capture them!
    # function m(){let e=([a-zA-Z0-9_]+)\.current\.uBend\.value,t=t=>{if(Math\.abs\(e\)<1e-6)return\{pos:new ([a-zA-Z0-9_]+)\(t,0,0\),rotY:0\};let n=1/e,r=t/n;return\{pos:new \2\(Math\.sin\(r\)\*n,0,Math\.cos\(r\)\*n\),rotY:r\}\};for\(let e of ([a-zA-Z0-9_]+)\.current\)\{let t=([a-zA-Z0-9_]+)\(e\.front\);\4\(e\.back\),e\.width=t\}let n=-\(\5\.current\.reduce\(\(e,t\)=>e\+t\.width,0\)\+\(\5\.current\.length-1\)\*([a-zA-Z0-9_]+)\)/2;
    
    pattern = r'function ([a-zA-Z0-9_]+)\(\)\{let ([a-zA-Z0-9_]+)=([a-zA-Z0-9_]+)\.current\.uBend\.value,([a-zA-Z0-9_]+)=\4=>\{if\(Math\.abs\(\2\)<1e-6\)return\{pos:new ([a-zA-Z0-9_]+)\(\4,0,0\),rotY:0\};let ([a-zA-Z0-9_]+)=1/\2,([a-zA-Z0-9_]+)=\4/\6;return\{pos:new \5\(Math\.sin\(\7\)\*\6,0,Math\.cos\(\7\)\*\6\),rotY:\7\}\};for\(let ([a-zA-Z0-9_]+) of ([a-zA-Z0-9_]+)\.current\)\{let ([a-zA-Z0-9_]+)=([a-zA-Z0-9_]+)\(\8\.front\);\11\(\8\.back\),\8\.width=\10\}let ([a-zA-Z0-9_]+)=-\(\9\.current\.reduce\(\(([a-zA-Z0-9_]+),([a-zA-Z0-9_]+)\)=>\13\+\14\.width,0\)\+\(\9\.current\.length-1\)\*([a-zA-Z0-9_]+)\)/2;'
    
    match = re.search(pattern, js)
    if match:
        funcName = match.group(1)   # m
        uBendLocal = match.group(2) # e
        refBase = match.group(3)    # j
        tParam = match.group(4)     # t
        vectorClass = match.group(5)# X
        nLocal = match.group(6)     # n
        rLocal = match.group(7)     # r
        eItem = match.group(8)      # e
        zRef = match.group(9)       # z
        tWidth = match.group(10)    # t
        pFunc = match.group(11)     # p
        nOut = match.group(12)      # n
        eRed = match.group(13)      # e
        tRed = match.group(14)      # t
        gapWorld = match.group(15)  # o
        
        replacement = f"function {funcName}(){{for(let {eItem} of {zRef}.current){{let {tWidth}={pFunc}({eItem}.front);{pFunc}({eItem}.back),{eItem}.width={tWidth}}}let _tC={zRef}.current.reduce(({eRed},{tRed})=>{eRed}+{tRed}.width,0)+{zRef}.current.length*{gapWorld};let _pR=_tC/(2*Math.PI);{refBase}.current.uBend.value=1/_pR;let {uBendLocal}={refBase}.current.uBend.value,{tParam}={tParam}=>{{if(Math.abs({uBendLocal})<1e-6)return{{pos:new {vectorClass}({tParam},0,0),rotY:0}};let {nLocal}=1/{uBendLocal},{rLocal}={tParam}/{nLocal};return{{pos:new {vectorClass}(Math.sin({rLocal})*{nLocal},0,Math.cos({rLocal})*{nLocal}),rotY:{rLocal}}}}};let {nOut}=-(_tC-{gapWorld})/2;"
        
        new_js = js[:match.start()] + replacement + js[match.end():]
        print(f"Patched Menu3D math in {fname}")
        
        # Save fixed JS file directly to export directory
        out_path = os.path.join(export_dir, fname)
        open(out_path, 'w', encoding='utf-8').write(new_js)
    else:
        print(f"Could not find exact layout match in {fname}")

# Now patch the imported remote URLs in index.html and all other html files to point locally
for root, dirs, files in os.walk(export_dir):
    for f in files:
        if f.endswith('.html'):
            html_path = os.path.join(root, f)
            html = open(html_path, encoding='utf-8').read()
            html = html.replace('https://framerusercontent.com/sites/2TJlmTmK48T8qzgHcPm2Tm/script_main.zMWyeqfe.mjs', '/script_main.zMWyeqfe.mjs')
            html = html.replace('https://framerusercontent.com/sites/2TJlmTmK48T8qzgHcPm2Tm/script_main.D_QN_HoU.mjs', '/script_main.D_QN_HoU.mjs')
            open(html_path, 'w', encoding='utf-8').write(html)
            
print("Done patching html files.")
