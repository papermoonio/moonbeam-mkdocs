# ------------ 👋 Welcome to the script for moving pages in the chinese repo ------------ #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to automatically update page(s) in the Chinese repo       #
# whenever page(s) are moved in the English repo. It updates the location of the page,    #
# any image paths that may have been changed, and any .pages files that need to be        #
# updated. It does so by comparing two commits and getting all of the changed files       #
# and sorting through them.                                                               #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs-cn` repo is nestled inside of the     #
#  `moonbeam-mkdocs` repo. Then simply run the following command:                         #
# `python scripts/move-pages.py <prev_commit> <latest_commit>` passing in the hash        #
#  of the two commits to compare. When the script is finished, the changes will be in the #
# `moonbeam-docs-cn` repo for you to review and commit them. That's it!                   #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

import os
import sys
import requests

first_commit = sys.argv[1]
last_commit = sys.argv[2]
print("✅ Fetching updated files")
files = requests.get("https://api.github.com/repos/moonbeam-foundation/moonbeam-docs/compare/" + first_commit + "..." + last_commit).json().get("files")

modified_files = []
removed_files = []
renamed_files = []
renamed_images = []
added_files = []

class Renamed:
    def __init__(self, previous_path, current_path):
        self.previous_path = previous_path
        self.current_path = current_path

class Renamed_Image:
    def __init__(self, file_path, previous_path, current_path):
        self.file_path = file_path
        self.previous_path = previous_path
        self.current_path = current_path

class Modified:
    def __init__(self, file_path, patch):
        self.file_path = file_path
        self.patch = patch

print("✅ Sorting updated files")
for file in files:
    status = file.get("status")
    filename = file.get("filename")

    # don't worry about code snippets or index page images
    if "snippets/code" not in filename and "/index-pages/" not in filename:
        if status == "added":
            added_files.append(filename)
        elif status == "removed":
            removed_files.append(filename)
        elif status == "renamed":
            if "images/" in filename:
                # save the filename where the images need to be updated, plus the before and after image path
                file_path = filename[:filename.rfind('/')] + ".md"
                file_path = file_path.replace("images/", "")
                renamed = Renamed_Image(file_path, file.get("previous_filename"), filename)
                renamed_images.append(renamed)
            else:
                renamed = Renamed(file.get("previous_filename"), filename)
                renamed_files.append(renamed)
        elif status == "modified":
            # only handle modified .pages files
            if ".pages" in filename:                
                modified = Modified(filename, file.get("patch"))
                modified_files.append(modified)


root = "moonbeam-docs-cn/"

print("✅ Adding new files")
# For additions, add the file to the Chinese repo
for file in added_files:
    # Check to make sure the parent directory exists
    # > If it does, go ahead and add the file
    # > If it doesn't, create the directory and then add the file 
    directory_path = root + file[:file.rfind('/')]
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
    with open(root + file, 'w'):
        pass


print("✅ Removing deleted files")
# For removals, remove the file from the Chinese repo & then check if the parent
# directory is empty
# > If it's empty then delete the directory
for file in removed_files:
    # if the file is an image, it can be skipped because those have already been removed in the English repo
    if (file.startswith('images/')):
        continue
    os.remove(root + file)

    directory_path = root + file[:file.rfind('/')]
    if len(os.listdir(directory_path)) == 0:
        os.rmdir(directory_path)


print("✅ Renaming moved files")
# For renamed files, rename the file but first make sure that the parent directory
# exists
# > If it doesn't exist, create it
# Then check to make sure that the parent directory is not empty
# > If it's empty, delete the directory
for file in renamed_files:
    curr_directory_path = root + file.current_path[:file.current_path.rfind('/')]
    if not os.path.exists(curr_directory_path):
        os.makedirs(curr_directory_path)

    os.rename(root + file.previous_path, root + file.current_path)

    prev_directory_path = root + file.previous_path[:file.previous_path.rfind('/')]
    if len(os.listdir(prev_directory_path)) == 0:
        os.rmdir(prev_directory_path)

print("✅ Renaming moved images")
# For renamed images, open the file where the images have been renamed and then
# find the old image path and replace it with the new one and save the file
for image in renamed_images:
    changed_file_path = root + image.file_path
    content = ""

    file = open(changed_file_path, "r")
    for line in file:
        if "](/images/" in line:
            # grab just the image path
            if image.previous_path in line:
                line = line.replace(image.previous_path, image.current_path)
        content += line  
    file.close()

    write_file = open(changed_file_path, "w")
    write_file.write(content)
    write_file.close()


print("✅ Modifying .pages files")
# For modified .pages file, make the necessary modifications and save the file
# > If a line has been deleted, delete it
# > If a line has been added, add it
for pages_file in modified_files:
    file_path = root + pages_file.file_path
    content = ""

    file = open(file_path, "r")
    patch = pages_file.patch.split('\n')
    
    new_line = ""
    for f_line in file:
        if f_line.startswith("title") or f_line.startswith("hide") or f_line.startswith("nav") or "index.md" in f_line:
            content += f_line
            continue
        for p_line in patch:
            if not p_line.startswith("+") and not p_line.startswith("-") and f_line in p_line:
                content += f_line
            elif p_line.startswith("+"):
                new_line = p_line[1:] + "\n"
            elif p_line.startswith("-") and f_line in p_line:
                pass
            else:
                new_line = f_line
    
        content += new_line
    
    file.close()
    write_file = open(file_path, "w")
    write_file.write(content)
    write_file.close()

print("✅ Request completed! Please check out the changes in the chinese repo!")