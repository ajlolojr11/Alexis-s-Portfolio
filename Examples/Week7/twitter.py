# Uses re.sub

'''
import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")'''

# Uses capture group

import re

url = input("URL: ").strip()

if matches:= re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_\.]+)", url, re.IGNORECASE):
    print("Username:", matches.group(1))
