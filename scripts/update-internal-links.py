# ---------------------- 👋 Welcome to the script for updating Markdown links ----------------------- #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to search through all Markdown (.md) files in a given directory       #
# and modify certain URL links that follow the `](/...` syntax. Specifically, it searches for links   #
# that do not start with `](/images/` and either contain a `#` or don't. For links containing a `#`,  #
# the script adds a `/` before the `#` symbol if one is not already present. For links without a `#`, #
# it adds a `/` before the closing parenthesis. URLs starting with `](/images/` are ignored.          #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use this script, provide the path to the directory containing your Markdown files. The script    #
# will process each `.md` file in the directory, making the necessary URL modifications directly      #
# in the files. Simply run the script in your terminal, and any relevant URLs will be updated.        #
# --------------------------------------------------------------------------------------------------- #

import os
import re

# Function to process each .md file and update URLs
def process_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex to match the ](/ syntax
    pattern = r'\]\(/\S+?\)'

    def replace_url(match):
        url = match.group(0)
        # Check if the URL starts with ](/images/
        if url.startswith('](/images/'):
            return url
        
        # Find the URL inside the parentheses
        inner_url = re.search(r'\(/\S+?\)', url).group(0)

        # Check if the URL contains a #
        if '#' in inner_url:
            # Add a / before the # if it's not already there
            if '/#' not in inner_url:
                inner_url = inner_url.replace('#', '/#')
        else:
            # Add a / before the closing parenthesis if not already present
            if not inner_url.endswith('/)'):
                inner_url = inner_url[:-1] + '/)'

        # Replace the old URL with the updated one
        url = re.sub(r'\(/\S+?\)', inner_url, url)

        return url

    # Apply the regex replacement
    updated_content = re.sub(pattern, replace_url, content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# Function to walk through the directory and process each .md file
def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_md_file(file_path)
                print(f"Processed: {file_path}")

# Directory to search through
directory_to_process = './moonbeam-docs/'

# Run the script on the directory
process_directory(directory_to_process)
