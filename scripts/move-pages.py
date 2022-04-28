# ------------ 👋 Welcome to the script for moving pages in the chinese repo ------------ #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to automatically update page(s) in the Chinese repo       #
# whenever page(s) are moved in the English repo. It only updates the location of the     #
# page, keeping the content in tact.                                                      #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` and `moonbeam-docs-cn` repos are     #
# nestled inside of the `moonbeam-mkdocs` repo. Then simply run the following command:    #
# `python scripts/compress-images.py <branch>` passing in the name of the branch with the #
# changes in the English repo, even if it's master, in your terminal. When the script is  #
# finished, the files without a match will be printed to your terminal. Just take some    #
# time to review those files. Then you can commit the changes in the `moonbeam-docs-cn`   #
# repo! That's it!                                                                        #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

import os
import requests
import sys
import shutil

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
                if "/legacy/" not in current_file and ".DS_Store" not in current_file and ".svg" not in current_file and ".snippets/code/" not in current_file:
                    current_file_paths.append(current_file)

    return current_file_paths


# Function to get the previous file paths from `master`
def fetch_previous_file_paths():
    previous_file_paths = []
    # Get the sha of the `master` branch so it can be used in the following calls
    sha = requests.get(
        "https://api.github.com/repos/PureStake/moonbeam-docs/branches/" + sys.argv[1]).json()["commit"]["sha"]

    # Get file structure from the `master` branch and iterate over it
    root_tree = requests.get(
        "https://api.github.com/repos/PureStake/moonbeam-docs/git/trees/" + sha + "?recursive=1").json()["tree"]
    for item in root_tree:
        path = item["path"]
        # Filter out directories
        if not path.startswith(tuple(omit_dirs)) and "images/legacy/" not in path and ".snippets/code/" not in path and path.endswith(tuple(path_endings)):
            previous_file_paths.append(path)

    return previous_file_paths


# Function to actually move the pages
def handle_page_moves(moved_pages):
    for page in moved_pages:
        # get directory
        prev_dir = page.previous_path[:page.previous_path.rfind('/')]
        curr_dir = page.current_path[:page.current_path.rfind('/')]
        full_prev_dir = "moonbeam-docs-cn/" + prev_dir
        full_curr_dir = "moonbeam-docs-cn/" + curr_dir

        if os.path.exists(full_curr_dir):
            # > If the directory already exists, no need to create a new one just
            # need to move the page to the dir and update the .pages file for the
            # previous and current directories
            curr_pages_file = open(full_curr_dir + "/.pages", "a")
            prev_pages_file = open(full_prev_dir + "/.pages", "r")
            pages_entry = ""
            prev_pages_content = ""

            # update the existing .pages file
            prev_file = page.previous_path.split("/")[-1]
            for line in prev_pages_file:
                if prev_file in line:
                    pages_entry = line
                else:
                    prev_pages_content += line

            prev_pages_file.close()

            prev_pages_file = open(full_prev_dir + "/.pages", "w")
            prev_pages_file.write(prev_pages_content)
            prev_pages_file.close()

            # update the current .pages file
            curr_pages_file.write("\n" + pages_entry)
            curr_pages_file.close()

            # move the page
            os.rename("moonbeam-docs-cn/" + page.previous_path,
                      "moonbeam-docs-cn/" + page.current_path)
        else:
            # > If the directory doesn't exist, the directory (and any prior directories)
            # must be created & then the file can be moved
            os.makedirs(full_curr_dir)

            # move all pages that need to be moved to this new directory by
            # finding all `current_path`s that have the same directory, if any
            filtered = [p for p in moved_pages if curr_dir in p.current_path]
            for p in filtered[:]:
                os.rename("moonbeam-docs-cn/" + p.previous_path,
                          "moonbeam-docs-cn/" + p.current_path)
                filtered.remove(p)
                moved_pages.remove(p)

            # check if the previous directory is empty, if so delete it
            if len(os.listdir(full_prev_dir)) == 0:
                os.rmdir(full_prev_dir)

                # if a directory was deleted, it needs to be removed from the parent .pages file
                parent_dir = full_prev_dir[:full_prev_dir.rfind('/')]
                prev_dir_name = "  - " + full_prev_dir.split("/")[-1]
                parent_path = parent_dir + "/.pages"

                parent_pages_file = open(parent_path, "r")
                parent_pages_content = ""

                for line in parent_pages_file:
                    if prev_dir_name.strip() != line.strip():
                        parent_pages_content += line

                parent_pages_file.close()

                parent_pages_file = open(parent_path, "w")
                parent_pages_file.write(parent_pages_content)
                parent_pages_file.close()


# Check the leftover pages to see if they exist in the Chinese site or not
# > If they don't exist, that means they are new files that need to be translated
# > If they exist, then they are old pages that have been deleted in the english
# repo and need to be deleted in the chinese repo
def check_leftover_pages(previous, current):
    print("⚠️ Couldn't find a match for the following files:")
    for previous_file in previous:
        full_prev_path = "moonbeam-docs-cn/" + previous_file
        if os.path.exists(full_prev_path):
            os.remove(full_prev_path)
        else:
            print(
                "This file has just been added and will need to be translated: ", previous_file)
            # create any new directories if needed, if not this command doesn't change anything
            os.makedirs(full_prev_path.split("/")[-2])
            # copy and move the new file from english repo to chinese repo
            shutil.copy("moonbeam-docs/" + previous_file, full_prev_path)

    # There shouldn't be any current files left, if there are log them for manual review
    for current_file in current:
        print("Please manually review this file: ", current_file)


class Moved:
    def __init__(self, previous_path, current_path):
        self.previous_path = previous_path
        self.current_path = current_path


def main():
    print("🗃 Fetching file structure for comparison...")

    if len(sys.argv) == 1:
        raise Exception(
            "Please provide the branch for the english repo changes")

    previous = fetch_previous_file_paths()
    current = fetch_current_file_paths()

    moved_pages = []

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
                moved_page = Moved(previous_file, current_file)
                moved_pages.append(moved_page)

    # Filter through the leftover matches, look for just the filename
    for previous_file in previous[:]:
        prev_file_name = previous_file.split("/")[-1]
        for current_file in current[:]:
            curr_file_name = current_file.split("/")[-1]

            if (prev_file_name == curr_file_name):
                previous.remove(previous_file)
                current.remove(current_file)
                moved_page = Moved(previous_file, current_file)
                moved_pages.append(moved_page)

    handle_page_moves(moved_pages)

    # Filter through any other remaining files & print them to the terminal
    if len(previous) > 0 or len(current) > 0:
        check_leftover_pages(previous, current)

    print("✅ Request completed! Please check out the changes in the moonbeam-docs-cn repo")


main()
