# ---------------- 👋 Welcome to the script for updating redirects ------------------#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to automatically update the `redirects.json` file   #
# based on changes in a pull request. It checks for files that have been removed    #
# or renamed and adds or updates redirects accordingly.                             #
#                                                                                   #
# For removed files:                                                                #
#   - Any existing redirects pointing to the removed file will be updated to        #
#     "TODO: UPDATE_ME" (a placeholder requiring human review).                     #
#   - A new redirect will be added with the removed file path as the `key` and      #
#     "TODO: UPDATE_ME" as the `value`.                                             #
#                                                                                   #
# For renamed files:                                                                #
#   - Any existing redirects pointing to the old file path will be updated to the   #
#     new path.                                                                     #
#   - A new redirect will be added with the old file path as `key` and the new path #
#     as `value`.                                                                   #
#                                                                                   #
# To use the script, simply run:                                                    #
#   python scripts/update-redirects.py <PR_NUMBER> <OWNER> <REPO>                   #
#                                                                                   #
# Command-line arguments:                                                           #
#   - `PR_NUMBER`: Pull request number to analyze                                   #
#   - `OWNER`: GitHub repository owner                                              #
#   - `REPO`: GitHub repository name                                                #
#                                                                                   #
# Example usage:                                                                    #
#   python scripts/update-redirects.py 42 moonbeam-foundation moonbeam-docs         #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


import json
import sys
from pathlib import Path
import requests

REDIRECTS_FILE = "redirects.json"
IGNORED_FOLDERS = {"images", "js", "scripts", "run"}


def is_ignored(filepath: str) -> bool:
    """Skip hidden files/folders or certain top-level folders."""
    parts = filepath.split("/")
    if any(part.startswith(".") for part in parts):
        return True
    if parts[0] in IGNORED_FOLDERS:
        return True
    return False


def format_path(path: str) -> str:
    """Convert a file path into '/path/to/file/' format (remove .md extension, drop 'index')."""
    path = path.strip()
    if path.endswith(".md"):
        path = path[:-3]
    # If the file is 'index' at the end, drop it
    if path.endswith("index"):
        path = path[: -len("index")].rstrip("/")
    return "/" + path.strip("/") + "/"


def load_redirects():
    if Path(REDIRECTS_FILE).exists():
        with open(REDIRECTS_FILE, "r") as f:
            return json.load(f)
    return {"data": []}


def save_redirects(data):
    data["data"].sort(key=lambda r: r["key"])
    with open(REDIRECTS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def fetch_pr_files(owner: str, repo: str, pr_number: str):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    files = []
    page = 1

    while True:
        resp = requests.get(url, params={"page": page, "per_page": 100})
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        files.extend(data)
        page += 1
    return files


def process_pr(owner: str, repo: str, pr_number: str):
    pr_files = fetch_pr_files(owner, repo, pr_number)
    redirects = load_redirects()
    existing = redirects["data"]

    original_count = len(existing)
    modified_count = 0
    added_count = 0
    added_redirects = []

    for f in pr_files:
        status = f.get("status")
        old_path = f.get("previous_filename")
        new_path = f.get("filename")

        if status not in {"removed", "renamed"}:
            continue  # only care about removed/renamed

        # Skip ignored files
        if new_path and is_ignored(new_path):
            continue
        if old_path and is_ignored(old_path):
            continue

        if status == "removed":
            formatted = format_path(new_path)
            for redirect in existing:
                if redirect["value"] == formatted:
                    redirect["value"] = "TODO: UPDATE_ME"
                    modified_count += 1
            new_redirect = {"key": formatted, "value": "TODO: UPDATE_ME"}
            existing.append(new_redirect)
            added_redirects.append(new_redirect)
            added_count += 1

        elif status == "renamed":
            # Apply format_path to both old and new paths, handles index.md as well
            formatted_old = format_path(old_path)
            formatted_new = format_path(new_path)
            for redirect in existing:
                if redirect["value"] == formatted_old:
                    redirect["value"] = formatted_new
                    modified_count += 1
            new_redirect = {"key": formatted_old, "value": formatted_new}
            existing.append(new_redirect)
            added_redirects.append(new_redirect)
            added_count += 1

    save_redirects(redirects)

    print(f"✅ Redirects updated for PR #{pr_number} in repo {owner}/{repo}")

    print(f"\n🔢 Stats:")
    print(f"Original redirects: {original_count}")
    print(f"Redirects modified: {modified_count}")
    print(f"Redirects added: {added_count}")
    print(f"Total redirects now: {len(redirects["data"])}")

    if added_redirects:
        print("\n⚠️ Redirects that need attention:")
        for r in added_redirects:
            print(f"key: {r['key']}, value: {r['value']}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python scripts/update-redirects.py <PR_NUMBER> <OWNER> <REPO>")
        sys.exit(1)

    pr_number = sys.argv[1]
    owner = sys.argv[2]
    repo = sys.argv[3]

    process_pr(owner, repo, pr_number)
