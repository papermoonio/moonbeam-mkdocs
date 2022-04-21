# ------------ 👋 Welcome to the script for moving pages in the chinese repo ------------ #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to automatically update page(s) in the Chinese repo       #
# whenever page(s) are moved in the English repo. It only updates the location of the     #
# page, keeping the content in tact.                                                      #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` and `moonbeam-docs-cn` repos are     #
# nestled inside of the `moonbeam-mkdocs` repo. Then simply run the following command:    #
# `python scripts/compress-images.py` in your terminal. When the script is finished, the  #
# files without a match will be printed to your terminal. Just take some time to review   #
# those files. Then you can commit the changes in the `moonbeam-docs-cn` repo! That's it! #

import os
import requests
import sys

# Function to filter root items & images
omit_dirs = ["js", "LICENSE", ".github", ".pages",
             "index.md", "README.md", "CONTRIBUTING.md", "images"]
path_endings = [".js", ".py", ".sol", ".md", ".pages"]


def filter_root_directories(variable):
    if variable not in omit_dirs and variable.find(".") == -1:
        return variable
    if variable == ".snippets" or variable == ".pages" or variable == "index.md":
        return variable

# Function to walk the directory and get current file paths
def fetch_current_file_paths():
    root_items = os.listdir('moonbeam-docs')
    filtered_directories = list(filter(filter_root_directories, root_items))
    current_file_paths = []

    for dir in filtered_directories:
        for root, dirs, files in os.walk('moonbeam-docs/' + dir):
            root_copy = root.split("/")
            root_copy.pop(0)
            root = "/".join(root_copy)

            # Write files to json output file
            for f in files:
                # Add file path to array of files
                current_file = root + "/" + os.path.basename(f)
                if "/legacy/" not in current_file and ".DS_Store" not in current_file and ".svg" not in current_file:
                    current_file_paths.append(current_file)

    return current_file_paths

# Function to get the previous file paths from `master`
def fetch_previous_file_paths():
    previous_file_paths = []
    # Get the sha of the `master` branch so it can be used in the following calls
    sha = requests.get(
        "https://api.github.com/repos/PureStake/moonbeam-docs/branches/master").json()["commit"]["sha"]

    # Get file structure from the `master` branch and iterate over it
    root_tree = requests.get(
        "https://api.github.com/repos/PureStake/moonbeam-docs/git/trees/" + sha + "?recursive=1").json()["tree"]
    for item in root_tree:
        path = item["path"]
        # Filter out directories
        if not path.startswith(tuple(omit_dirs)) and "images/legacy/" not in path and path.endswith(tuple(path_endings)):
            previous_file_paths.append(path)

    return previous_file_paths


def main():
    print("🗃 Fetching file structure for comparison...")

    previous = fetch_previous_file_paths()
    current = fetch_current_file_paths()

    # Remove exact matches
    for previous_file in previous[:]:
        for current_file in current[:]:
            if (previous_file == current_file):
                previous.remove(previous_file)
                current.remove(current_file)

    # Filter through the leftover matches, look for subdirectory/file
    for previous_file in previous[:]:
        prev_dir_name = previous_file.split("/")[-2]
        prev_file_name = previous_file.split("/")[-1]
        prev_path = prev_dir_name + "/" + prev_file_name

        for current_file in current[:]:
            curr_dir_name = current_file.split("/")[-2]
            curr_file_name = current_file.split("/")[-1]
            curr_path = curr_dir_name + "/" + curr_file_name

            if (prev_path == curr_path):
                previous.remove(previous_file)
                current.remove(current_file)

                # Need to figure out how to rename the file appropriately
                os.rename("moonbeam-docs-cn/" + previous_file,
                          "moonbeam-docs-cn/" + current_file)

    # Filter through the leftover matches, look for just the filename
    for previous_file in previous[:]:
        prev_file_name = previous_file.split("/")[-1]
        for current_file in current[:]:
            curr_file_name = current_file.split("/")[-1]

        if (prev_file_name == curr_file_name):
            os.rename("moonbeam-docs-cn/" + previous_file,
                      "moonbeam-docs-cn/" + current_file)

    # Filter through any other remaining files & print them to the terminal
    print("⚠️ Couldn't find a match for the following files:")
    for previous_file in previous:
        print("Pre-existing file: ", previous_file)
    for current_file in current:
        print("New file: ", current_file)


main()
