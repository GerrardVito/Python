import re

# Example string
text = "The population is 19 x^2"

# Search for numbers in the tens, hundreds, and thousands range
pattern = r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b"

# Find all matches
matches = re.findall(pattern, text)

# Print the matches
for match in matches:
    print(match)
