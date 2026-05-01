import re

content = open('index.html', encoding='utf-8').read()

# The real fix: The 3D canvas reads the parent container's innerText
# which chains ALL nav items together
# The parent container has class framer-190oa1v (original nav container)
# The canvas plugin likely queries all h6 elements in its container

# DIFFERENT APPROACH: Instead of modifying the spans (which are absolute positioned
# and contribute to innerText but are not visible in canvas), 
# we need to add a VISIBLE text gap INSIDE the h6 text flow

# The correct fix is to change these:
# >Home<span...>...</span></h6>
# to:
# >Home<span style="letter-spacing:138px;"> </span></h6>
# This adds a real space character with 138px letter-spacing
# Since it's INLINE (not absolute), the canvas text engine will see it

# But actually the canvas reads the DOM textContent
# textContent of ">Home<span...> </span></h6>" would be "Home  " with some spaces
# The canvas then draws each item as concatenated text

# THE REAL ISSUE: The canvas probably reads ALL h6 elements' textContent COMBINED
# So we need to ensure the separator IS in the text
# The 3 nbsp in the current span ARE in textContent

# Let's verify: does the current span content show in browser's getComputedText?
# Since position:absolute content IS in innerText/textContent

# Actually looking at the screenshot, "Contact" and "ntact" are visible separately
# This confirms the items ARE being separated, just not by 138px

# The REAL issue: The canvas is rendering correctly but the "word gap" from Framer 
# controls actual spacing between words/letters in their 3D canvas engine
# The span approach will never work because the canvas engine in Framer's 3D plugin
# directly reads the h6 textContent and then draws with its own font metrics

# The correct approach: modify the word gap WITHIN the canvas script's configuration
# But that's in Framer's CDN...

# ALTERNATIVE: Make the gap visible by using zero-width characters that have width
# Let's try: add many regular spaces (actual space chars) between words
# These spaces WILL be captured by textContent and drawn by canvas

# Find the pattern and add spaces via the span
old_span = '<span class="nav-3d-spacer" style="opacity:0.01;position:absolute;pointer-events:none;">&nbsp;&nbsp;&nbsp;</span>'
# Replace with visible space that takes up real width in canvas text
# Use em-space (U+2003) which is about 1em wide, repeat for ~138px gap at 222px font
# 138/222 ≈ 0.62 em, em-space is 1em, so roughly 1 em-space would be too much
# Try thin spaces or figure spaces
# At 222px font: 1 em ≈ 222px, so 138px ≈ 0.62em 
# Use 2x en-spaces (U+2002, ~0.5em each) = ~1em = ~222px - too much
# Use 1 en-space = ~111px, still too much
# Use 1 thin space (U+2009, ~0.2em) = 44px, too little
# Use 3 thin spaces = ~133px, close to 138px!
# Or: 1 en-space + 1 thin space = ~111 + 44 = ~155px 
# Or: just use regular word spacing: spaces render at about 0.25em at normal weight
# 138 / 222 = 0.62em, at 0.25em per space that's about 2.5 spaces, use 3 spaces

new_span = '<span class="nav-3d-spacer" style="opacity:0.01;position:absolute;pointer-events:none;">\u2005\u2005\u2005\u2005\u2005\u2005\u2005</span>'
# \u2005 = four-per-em space (0.25em each)
# 7 × 0.25em × 222px = 388px - too large
# Let's use 3 four-per-em spaces = 3 × 0.25 × 222 = 166.5px ≈ close to 138px

new_span_3 = '<span class="nav-3d-spacer" style="opacity:0.01;position:absolute;pointer-events:none;">\u2005\u2005\u2005</span>'

count = content.count(old_span)
print(f"Found {count} occurrences")

if count > 0:
    new_content = content.replace(old_span, new_span_3)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Applied 3 four-per-em spaces as gap")
else:
    print("Pattern not found! Let me check current span...")
    # Check what we have now
    idx = content.find('nav-3d-spacer')
    if idx != -1:
        print(content[idx-50:idx+200])
