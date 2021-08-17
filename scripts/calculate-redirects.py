# ------------- 👋 Welcome to the script for calculating redirect mappings ---------------#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to calculate redirect mappings for the `mkdocs.yml` file. #
# The script works by looking at the current file directory in the `master` branch and    #
# on your local branch. It compares the two file structures to see if content has been    #
# moved at all. If any content has been moved, the script will try to match the moved     #
# content and add it to the `redirect_maps` config in `mkdocs.yml`.                       #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` repo is nestled inside of the        #
#  `moonbeam-mkdocs` repo and on your branch with the latest changes. Then simply run     #
# `python scripts/calculate-redirects.py` in your terminal. There will be logs printed to #
# the terminal. Please read through them as they will guide you on which redirects need   #
# to be manually reviewed and any possible duplicates to be reviewed as well.             #
# The `mkdocs.yml` will automatically be updated, so just open that file to see the new   #
# redirects and make any updates!                                                         #

import requests
import os
import yaml

# Function to filter root items to get rid of those including a ".", "snippets", "js", "images", and "dapps-list"
def filter_root_directories(variable):
    omit_dirs = ["snippets", "js", "images", "dapps-list"]
    if ((variable not in omit_dirs) and (variable.find(".") == -1)):
        return variable

# Function to walk the directory and get current file paths
def fetch_current_file_paths():
    root_items = os.listdir('moonbeam-docs')
    filteredDirectories = list(filter(filter_root_directories, root_items))
    current_file_paths = []

    for dir in filteredDirectories:
        for root, dirs, files in os.walk('moonbeam-docs/' + dir):
            # Ignore dapps-list for right now
            if ("dapps-list" in root):
                break

            root_copy = root.split("/")
            root_copy.pop(0)
            root = "/".join(root_copy)

            # Write files to json output file
            for f in files:
                # Ignore .pages and index.md files
                if (f != ".pages") & (f != "index.md"):
                    # Add file path to array of files
                    current_file = root + "/" + os.path.basename(f)
                    current_file_paths.append(current_file)
                    # Write file path to JSON for future comparisons
                    current_file = '"' + current_file + '"'

    return current_file_paths

# Function to get the previous file paths from `master`
def fetch_previous_file_paths():
  previous_file_paths = []
  # Get the sha of the `master` branch so it can be used in the following calls
  sha = requests.get("https://api.github.com/repos/PureStake/moonbeam-docs/branches/master").json()["commit"]["sha"]

  # Get file structure from the `master` branch
  rootTree = requests.get("https://api.github.com/repos/PureStake/moonbeam-docs/git/trees/" + sha + "?recursive=1").json()["tree"]

  for item in rootTree:
    omit_dirs = ["snippets", "js", "images", "dapps-list", ".", "README.md"]
    path = item["path"]
    if not path.startswith(tuple(omit_dirs)) and path.endswith(".md"):
      previous_file_paths.append(path)

  return previous_file_paths

print("🗃 Fetching file structure for comparison...")

# Arrays of previous and current file paths
previous = fetch_previous_file_paths()
current = fetch_current_file_paths()
# Array for redirects
redirect_map = []
possible_dupes_map = []

# Class defintion for redirects and the redirect_map
class Redirect:
    def __init__(self, previous_path, current_path):
        self.previous_path = previous_path
        self.current_path = current_path

print("📁 Comparing files to find where content has moved...")

# Filter out exact matches
for previous_file in previous[:]:
    for current_file in current[:]:
        # Remove exact matches
        if (previous_file == current_file):
            previous.remove(previous_file)
            current.remove(current_file)

# Find directories that have moved
for previous_file in previous[:]:
    for current_file in current[:]:
        current_file_name = "/".join(current_file.split("/")[-2:]) # removes directory in root, keeps remainder of the path

        if (current_file_name in previous_file):
          match = Redirect(previous_file, current_file)
          redirect_map.append(match)

          previous.remove(previous_file)
          current.remove(current_file)

# Find files that have moved
for previous_file in previous[:]:
    previous_file_name = "/".join(previous_file.split("/")[-1:]) # takes last item in path (the file name)
    for current_file in current[:]:
          current_file_name = "/".join(current_file.split("/")[-1:])
          if (previous_file_name == current_file_name):
              match = Redirect(previous_file, current_file)
              redirect_map.append(match)

              try:
                previous.remove(previous_file)
              except:
                possible_dupes_map.append(match)

              current.remove(current_file)

# Find files that have moved
for previous_file in previous[:]:
    previous_file_name = "/".join(previous_file.split("/")[-1:]).replace(".md", "") # takes last item in path (the file name without .md at the end)
    for current_file in current[:]:
          current_file_name = "/".join(current_file.split("/")[-1:]).replace(".md", "")
          if (current_file_name in previous_file_name) or (previous_file_name in current_file_name):
              match = Redirect(previous_file, current_file)
              redirect_map.append(match)

              try:
                previous.remove(previous_file)
              except:
                possible_dupes_map.append(match)

              current.remove(current_file)

print("")
print("🥳 File comparison complete! Found {} matches!".format(len(redirect_map)))
print("")

print("🔧 Modifying existing redirects...")
print("➕ Creating new redirects...")

mkdocs_yaml = yaml.unsafe_load(open("mkdocs.yml", "r"))
prev_mapping = mkdocs_yaml["plugins"][3]["redirects"]["redirect_maps"]
prev_values = list(prev_mapping.values())
prev_keys = list(prev_mapping.keys())

for i in range(len(prev_mapping)):
  for item in redirect_map:
    if (prev_values[i] == item.previous_path):
      match = Redirect(prev_keys[i], item.current_path)
      redirect_map.append(match)

new_dict = {}
for redirect in redirect_map:
  new_dict[redirect.previous_path] = redirect.current_path

mkdocs_yaml["plugins"][3]["redirects"]["redirect_maps"] = new_dict
with open("mkdocs.yml", "w") as f:
    yaml.dump(mkdocs_yaml, f, sort_keys=False, allow_unicode=True, indent=2)

print("✅ Successfully updated the mkdocs.yml file with new redirects")

print("")
print("------------------------------------")
print("")

print("Matches not found for the remaining previous items (have they been deleted or moved? We need to manually find a redirect for these files): ")
print(previous)

print("")
print("------------------------------------")
print("")

print("Matches not found for the remaining current items (are these new pages? We need to manually look and see if any old files corresponds to these new files): ")
print(current)

print("")
print("------------------------------------")
print("")

print("There are possible duplicates that need to be reviewed. Find these files in the 'redirect_maps' section of the mkdocs.yml file and verify any matches with these file names are correct: ")
for dupe in possible_dupes_map:
  print("Possible dupe: ", dupe.previous_path, dupe.current_path)