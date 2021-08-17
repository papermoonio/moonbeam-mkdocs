# ----------------- 👋 Welcome to the script for generating index pages ------------------#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to create index pages for each directory. The script      #
# works by looking at your local file directory in the nestled `moonbeam-docs` repo for   #
# any directories without a `index.md` file and generates one for that directory. 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` repo is nestled inside of the        #
#  `moonbeam-mkdocs` repo and on your branch with the latest changes. Then simply run     #
# `python scripts/create-index-pages.py` in your terminal. There will be logs printed to  #
# the terminal to let you know which index pages were created. If there weren't any       #
# created, there will be no output. You can head to the `moonbeam-docs` repo to see any   #
# newly generated files.                                                                  #

import os
from typing import Container

root_items = os.listdir('moonbeam-docs')

def filter_root_directories(variable):
    omit_dirs = ["js", "images", "snippets", "dapps-list"]
    if ((variable not in omit_dirs) and (variable.find(".") == -1)):
        return variable

def create_index_page(path, dirname):
  if (not os.path.exists(path)):
      new_file_for_dir = open(path, "w+")
      readable_dir = dirname.replace("-", " ").title()

      if (readable_dir in "Openzeppelin"):
        readable_dir = "OpenZeppelin"

      new_file_for_dir_content =  "---\ntitle: " + readable_dir.title() + "\ntemplate: main.html\n---\n\n<div class='subsection-wrapper'></div>"
      new_file_for_dir.write(new_file_for_dir_content)
      print("Created index page: " + path)

filtered_directories = list(filter(filter_root_directories, root_items))

for dir in filtered_directories:
    create_index_page("moonbeam-docs/" + dir + "/index.md", dir)
        
    for root, dirs, files in os.walk('moonbeam-docs/' + dir):
      if ("dapps-list" in root):
        continue
      elif (len(dirs) > 0):
        filtered_subdirs = list(filter(filter_root_directories, dirs))
        for subdir in filtered_subdirs:
          create_index_page(root +  "/" + subdir + "/index.md", subdir)
        