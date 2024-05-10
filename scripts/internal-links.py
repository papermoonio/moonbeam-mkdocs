# ------------- 👋 Welcome to the script for calculating redirect mappings ---------------#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to add backslashes to the end of all internal links. This #
# is required because if there isn't a backslash, a redirect occurs and adds one.         #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` repo is nestled inside of the        #
#  `moonbeam-mkdocs` repo and on your branch with the latest changes. Then simply run     #
# `python scripts/internal-links.py` in your terminal. There will be logs printed to the  #
# terminal. When the script is complete, you can review all of the changes in the         #
# `moonbeam-docs` repo.                                                                   #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

import os
import re

# Function to recursively traverse directories
def traverse_dir(dir_path):
    print("👀 Scanning and updating links...")
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                modify_links(file_path)
    print("✅ All links have been updated")

# Function to modify links in Markdown content
def modify_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regular expression to match links that start with "](/"
    regex = r'\]\((?!/images/)(/[^#\s)]+)(?=[\s)]|$)'

    # Replace links according to the specified format
    modified_content = re.sub(regex, lambda match: match.group(0) + '/' if not match.group(0).endswith('/') else match.group(0), content)

    # Write modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)

# Start traversing from the current directory
traverse_dir('moonbeam-docs')
