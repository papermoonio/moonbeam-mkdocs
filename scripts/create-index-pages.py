import os
from typing import Container

root_items = os.listdir('moonbeam-docs')

def filter_root_directories(variable):
    omit_dirs = ["js", "images", "snippets", "dapps-list"]
    if ((variable not in omit_dirs) and (variable.find(".") == -1)):
        return variable

filteredDirectories = list(filter(filter_root_directories, root_items))

for dir in filteredDirectories:
    for root, dirs, files in os.walk('moonbeam-docs/' + dir):
      if ("dapps-list" in root):
        continue
      elif (len(dirs) > 0):
        filteredSubdirs = list(filter(filter_root_directories, dirs))
        for subdir in filteredSubdirs:
          if (os.path.exists(root +  "/" + subdir + "/index.md")):
            print("TRUE")

          new_file_for_subdir = open(root + "/" + subdir + "/index.md", "w+")
          readable_subdir = subdir.replace("-", " ").title()
          if (readable_subdir in "Openzeppelin"):
            readable_subdir = "OpenZeppelin"

          new_file_for_subdir_content =  "---\ntitle: " + readable_subdir.title() + "\ntemplate: main.html\n---\n\n<div class='subsection-wrapper'></div>"
          new_file_for_subdir.write(new_file_for_subdir_content)
