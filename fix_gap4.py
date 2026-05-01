import re

content = open('index.html', encoding='utf-8').read()

# The current span uses position:absolute which means:
# - textContent includes it 
# - innerText may NOT include it (browser treats absolute as non-rendered)
# Even if textContent gets it, the canvas code may use innerText
# 
# Solution: Remove position:absolute but keep opacity near 0
# Use display:inline-block with tiny height, so it's in the text flow
# and WILL be captured by innerText
#
# Four-per-em space (U+2005) = \u2005 = 0.25em each
# At 222px font: each = 55.5px. 3 of them = 166.5px (close to 138px)
# Let's use 2 en-quad spaces (U+2000, 1 en = 0.5em) = 2 x 111px = 222px - too much
# Use 2 four-per-em spaces = 2 x 55.5 = 111px
# Use 1 en + 1 four-per-em = 111 + 55.5 = 166.5px
# Use 2 four-per-em + tweak... let's just try making it visible inline

# Current pattern (after last fix):
old_span = '<span class="nav-3d-spacer" style="opacity:0.01;position:absolute;pointer-events:none;">\u2005\u2005\u2005</span>'

# New: inline so innerText captures it, color transparent so invisible 
new_span = '<span class="nav-3d-spacer" style="color:transparent;font-size:inherit;display:inline">\u2005\u2005\u2005</span>'

count = content.count(old_span)
print(f"Found {count} occurrences")

if count > 0:
    new_content = content.replace(old_span, new_span)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Applied inline transparent spacing")
else:
    # Check what we have
    idx = content.find('nav-3d-spacer')
    if idx != -1:
        print("Current span:")
        print(repr(content[idx-50:idx+300]))
    else:
        print("nav-3d-spacer not found at all!")
