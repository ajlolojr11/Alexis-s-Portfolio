# Uses re.search

'''import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")'''

# Uses .group

import re

name = input("What's your name? ").strip()
if matches:= re.search(r"^(.+), (.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"
print(f"hello, {name}")
