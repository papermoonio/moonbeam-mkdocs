# ------------------ 👋 Welcome to the script for dumping image hashes -------------------#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to create hashes of all of the images in `moonbeam-docs`  #
# and save the hashes along with the current file path to be referenced by the            #
# `update-images.py` script. It works by getting all of the images from your local        #
# `moonbeam-docs/images` directory, sha256 hashing them, and dumping them into a .json    # 
# file in the `moonbeam-mkdocs/scripts/image-hashes` directory. This script also deletes  #
# any pre-existing files in the `image-hashes` directory before starting so the directory #
# doesn't get overloaded with .json files.                                                #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` repo is nestled inside of your local #
# `moonbeam-mkdocs` repo and on your branch with the latest changes. The idea of this     #
# script is to generate image hashes off of the master branch, and then check out to the  #
# new branch (with changes) and run the `update-images.py` script which will look at the  #
# .json file generated by this script to figure out what image paths need to be updated.  #
# So ensure that you are running this script on the branch where the previous changes     #
# live. Run `python scripts/dump-image-hashes.py` and check out the generated .json file  #
# in `moonbeam-mkdocs/scripts/image-hashes/` and then continue on to use the              #
# `update-images.py` script                                                               # 

import os
import hashlib
import time
import json

# Get image paths and hashes
current_hashes = {}
for root, dirs, files in os.walk('moonbeam-docs/images'):
  for file in files:
    file_path = root + "/" + file
    with open(file_path, "rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        current_hashes[readable_hash] = file_path

# Check the image-hashes directory and delete any existing data
dir = "scripts/image-hashes/"
for file in os.listdir(dir):
  os.remove(os.path.join(dir, file))

# Create file & dump image hashes
file_name = "scripts/image-hashes/" + str(time.time()) + ".json"
with open(file_name, "w+") as output_file:
  json.dump(current_hashes, output_file, indent=4)
