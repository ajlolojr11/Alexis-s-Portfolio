# Problem Set 7
# Program: Watch on YouTube
# Alexis Varas Ortiz
# Description: Convert the iframe HTML element, extract the source
# and convert it to a valid youtube link
import re
import sys


def main():
    try:
        print(parse(input("HTML: ")))
    except re.error as e:
        print("Invalid regular expression...", e)
        sys.exit(1)

def parse(s):
    if re.search(r"^<iframe.+></iframe>$", s, re.IGNORECASE):
        if match:= re.search(r"(https?://(www\.)?youtube\.com/embed)/\w+", s, re.IGNORECASE):
            match = re.sub(match.group(1), "https://youtu.be", match.group(0), re.IGNORECASE)
            return match

    return None


if __name__ == "__main__":
    main()
