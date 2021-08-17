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
        