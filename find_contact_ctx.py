content = open('index.html', encoding='utf-8').read()
# Find where Contact spacer is and show big context
idx = content.find('Contact<span class="nav-3d-spacer"')
if idx != -1:
    out = content[max(0, idx-500):idx+800]
    open('out_contact_ctx.txt', 'w', encoding='utf-8').write(out)
    print("Found at", idx)
else:
    print("NOT FOUND")
    # Show first 300 chars around 'Contact'
    idx2 = content.find('Contact')
    if idx2 != -1:
        open('out_contact_ctx.txt', 'w', encoding='utf-8').write(content[max(0,idx2-200):idx2+300])
        print("Plain Contact found at", idx2)
