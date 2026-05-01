import re

content = open('index.html', encoding='utf-8').read()

# "ContactHome" found at 47578 - this is likely from previous CSS fix comment
# But the issue is the 3D canvas rendering strips HTML, reads DOM text
# Let's look at what the h6 elements actually read as text
# The 3D component queries .innerText or similar

# Find all places where nav items appear without space
for pair in ['ContactHome', 'HomeContact', 'ContactCases', 'CasesPresence', 'PresenceHome']:
    positions = [m.start() for m in re.finditer(pair, content)]
    print(f"{pair}: {len(positions)} occurrences at {positions[:5]}")

# The real problem: The 3D canvas reads from the h6 element's innerText
# The span with opacity:0.01 is VISIBLE to innerText but absolute positioned
# So the text the canvas reads is: "Contact   " (with nbsp spaces)
# The issue must be that it reads the parent container's innerText

# Let's find the framer-ljc3kb-container which wraps the canvas
idx = content.find('framer-ljc3kb-container')
if idx != -1:
    print(f"\nframer-ljc3kb-container at {idx}")
    print(content[max(0, idx-1000):idx+100])
