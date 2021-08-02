# --- 👋 Welcome to the script for creating header attributes --- #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to create attributes for every    #
# header in every file. These attributes will be used to link to  #
# sections in all non-English language repositores. Allowing for  #
# the section headers to be translated to the given language.     #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` repo is      #
# nestled inside of the `moonbeam-mkdocs` repo. Then simply run   #
# `python scripts/create-header-attributes.py` in your terminal.  #
# Then open the `moonbeam-docs` repo to see the changes have been #
# made and are ready to commit. That's it!                        #

import os

def filter_root_directories(variable):
    omit_dirs = ["js", "images"]
    if ((variable not in omit_dirs) and (variable.find(".") == -1)):
        return variable


def add_attributes_to_file(root, f):
  # Ignore .pages and index.md files
    if (f != ".pages") & (f != "index.md"):
        filename = root + "/" + f
        file = open(filename, "r")

        content = ""

        # Read the content for each file, modify any headers, and save output to content variable
        for line in file:
            if (line.startswith("##")):
                # Remove line break from header and any white space at the end of the header
                if ("{: #" in line):
                  line = line.split("{")[0]

                line = line.replace("\n", "").strip()
                words = line.split(" ")

                new_words = []
                for word in words:
                    new_word = word.replace("(", "")
                    new_word = new_word.replace(")", "")
                    new_word = new_word.replace(".", "")
                    new_word = new_word.replace("'", "")
                    new_word = new_word.replace("?", "")
                    new_word = new_word.replace(":", "")
                    new_word = new_word.replace('"', "")
                    new_word = new_word.replace("/", "")
                    new_word = new_word.replace("&", "-")
                    if (new_word != "-") and (new_word != ""):
                        new_words.append(new_word.strip())

                # Create attribute from header
                attribute = new_words[1:]
                attribute = "-".join(attribute)
                attribute = "{: #" + attribute + " }"

                # Combine header and attribute and add line break back in
                new_line = line + " " + attribute.lower() + " \n"
                content += (new_line)
            else:
                content += (line)

        file.close()

        # Create a new file to write the modifications to
        new_filename = ""
        if (".md" in filename):
            new_filename = filename.replace(".md", "-new.md")
        elif (".py" in filename):
            new_filename = filename.replace(".py", "-new.py")
        elif (".js" in filename):
            new_filename = filename.replace(".js", "-new.js")
        elif (".sol" in filename):
            new_filename = filename.replace(".sol", "-new.sol")

        new_file = open(new_filename, "w")
        new_file.write(content)
        new_file.close()

        # Delete existing file
        os.remove(filename)

        # Rename the new file, essentially replacing the old file
        os.rename(new_filename, filename)


root_items = os.listdir('moonbeam-docs')
filteredDirectories = list(filter(filter_root_directories, root_items))

# Create attributes for the filtered directories
for dir in filteredDirectories:
    for root, dirs, files in os.walk('moonbeam-docs/' + dir):
        # Ignore dapps-list for right now
        if ("dapps-list" in root):
            break

        for f in files:
            add_attributes_to_file(root, f)

# Create attributes for the README.md file
add_attributes_to_file("moonbeam-docs/", "README.md")
