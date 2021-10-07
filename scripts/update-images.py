# ------------------ 👋 Welcome to the script for updating image paths -------------------#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to find where images have been moved to on the English    #
# repo and to make the same changes to image paths in the various language repos. The     #
# script works alongside the `dump-image-hashes.py` script. See that script for details.  #
# It works by looking at the image hashes dumped (from the English repo) in the           #
# `image-hashes` directory and comparing that to image hashes from your current English   #
# `moonbeam-docs` file structure. Images are matched based on their hashes and the paths  #
# of the images are then iterated over and updated in each of the lanugage repos.         #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` repo is nestled inside of your local #
# `moonbeam-mkdocs` repo and on your branch with the latest changes. Also make sure that  #
# each of the language repos are nestled inside your local `moonbeam-mkdocs` repo. You    #
# should have already run the `dump-image-hashes.py` script on master and checked out to  #
# your branch with the changes. Go back to the `moonbeam-mkdocs` repo and run             #
# `python scripts/update-images.py` in your terminal. There will be logs printed to the   #
# terminal. Please read through and review them as files without a match will be listed   #
# and need to be reviewed. The script might take a minute to run. Once it's finished you  #
# can checkout the changes in each of the language repos and go ahead and commit the      #
# changes manually from there.                                                            #

import os
import hashlib
import json

class Redirect:
    def __init__(self, previous_path, current_path):
        self.previous_path = previous_path
        self.current_path = current_path

# Iterate through current file structure of moonbeam-docs repo
# and save image paths and hashes to current_hashes dictionary
current_hashes = {}
for root, dirs, files in os.walk('moonbeam-docs/images'):
  for file in files:
    file_path = root + "/" + file
    with open(file_path, "rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        current_hashes[readable_hash] = file_path

# Get previous image hashes stored in the image-hashes directory
redirect_map = []
hash_file = os.listdir("scripts/image-hashes/")[0] # there should only be one file in the image-hashes directory
previous_hashes = json.load(open("scripts/image-hashes/" + hash_file))

# Iterate through the previously stored image paths and hashes.
# If we can successfully use the previous image hash to access an
# item in the current_hashes dictionary, then the image is the same,
# and the paths need to be saved in the redirect_map for later usage
unknown_files = []
for prev_key, prev_value in previous_hashes.items():
  try:
    curr_value = current_hashes[prev_key]
    image_redirect = Redirect(prev_value, curr_value)
    redirect_map.append(image_redirect)
    current_hashes.pop(prev_key)
  except:
    unknown_files.append(prev_value)

# Notify of files without matches
print("❌ The following files do not have a match. Please check if they have been deleted or recently added: ")
for file in unknown_files:
  print(file)

print("-----------------") 

print("❌ The following files must have been recently added. Please double check: ")
for file in current_hashes:
  print(current_hashes[file])

print("-----------------") 

print("Updating image paths in each of the language repos. This could take a couple minutes ⏳")

# Now that we have the redirect_map containing previous and current image paths
# We need to use these paths to update files in each of the language repos
languages = ["cn", "es", "fr", "ru"]

# Function to filter out certain directories that wouldn't contain a reference
# to an image
def filter_root_directories(variable):
    omit_dirs = ["js", "images"]
    if ((variable not in omit_dirs) and (variable.find(".") == -1)):
        return variable

# For each of the languages, iterate through the files, and update image paths
for language in languages:
  root_dir = "moonbeam-docs-" + language
  filtered_directories = list(filter(filter_root_directories, os.listdir(root_dir)))

  # Iterate through each of the root directories
  for dir in filtered_directories:
    # Iterate through each of the subdirectories and files
    for root, dirs, files in os.walk(root_dir + "/" + dir):
      # Iterate through each of the markdown files, read the contents and search
      # for references to the previous image path and replace it with the current
      # image path
      for file in files:
        if file.endswith(".md"):
          for redirect in redirect_map:  
            file_path = root + "/" + file
            f = open(file_path, 'r')
            filedata = f.read()

            previous = redirect.previous_path.replace("moonbeam-docs", "")
            current = redirect.current_path.replace("moonbeam-docs", "")

            if (filedata.find(previous) > -1):
              newdata = filedata.replace(previous, current)

              f = open(file_path, 'w')
              f.write(newdata)
              f.close()

print("Done ✅! Head to each of the language repos to check out the changes")
