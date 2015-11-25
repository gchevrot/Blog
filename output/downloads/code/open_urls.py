#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Script for Python 3
# Extract URLs from my urls.text file
# The result is in a file named extracted_urls.txt
# Example: ./open_urls.py urls.txt '# Reproducibility'
#

import sys
import re

# Verify that Python is version 3
assert sys.version[0] == '3', 'This script is written for Python 3!'

# The script expected 2 arguments: the URLs file and the URL theme (it
# preceeds the urls you want to open in the URLs file)
assert len(sys.argv) == 3, """
The script expects 2 arguments:\n the URLs file and the URL theme 
(it preceeds the urls you want to open in the URLs file)
NOTE: you should include the '#' for the URL theme.
Example: ./open_urls.py urls.txt '# Reproducibility'
"""

filename = sys.argv[1]
theme = sys.argv[2]

with open(filename, 'r') as f:
    urls = f.readlines()

# Find the line number corresponding to the theme we are interested in:
regex = r'' + theme
match = False
for cpt, url in enumerate(urls):
    # If the theme is found
    if re.match(regex, url):
        match = True
        #print(cpt)
        break

# Exit if theme is not in the file 
if not match:
    print("""The theme you asked for "{0}" is not in the file
          {1}""".format(sys.argv[2], sys.argv[1]))
    exit()

# Now, we know the rank (=cpt) corresponding to the theme we are interested in,
# so we will save the URLs until the first blank line in the file
# extracted_urls.txt:
regex = r'\n'
filename = 'extracted_urls.txt'
f = open(filename, 'w')
for url in urls[cpt+1:]:
    print(url)
    f.write(url)
    if re.match(regex, url):
        break
f.close() # Don't forget to close the file!

print("""You can now open the extracted URLs via this command line:
      open /Applications/Firefox.app $(cat extracted_urls.txt)
      NOTE: Open firefox before the previous command so firefox will open the
      URLs in tabs instead of sessions""")

