#  👋 Welcome to the script for converting images to webp format  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to convert images from png to     #
# webp format                                                     #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` repo is      #
# nestled inside of the `moonbeam-mkdocs` repo. Then simply run   #
# `python scripts/convert-png-to-webp.py` in your terminal. The   #
# script will check all of the images to see if there are any in  #
# png format and convert those to webp format. After the          #
# conversion is complete, the png image will be deleted. Once the #
# script is complete, you can commit the changes in your local    #
# `moonbeam-docs` repo! And that's it!                            #

from PIL import Image
import os


# Loop through PNG files in the input directory
def convert_images(input_dir):
    for png_file in os.listdir(input_dir):
        if png_file.endswith(".png"):
            # Get the full file paths
            png_path = os.path.join(input_dir, png_file)
            webp_path = os.path.join(input_dir, os.path.splitext(png_file)[0] + ".webp")

            # Open and save the image in WebP format
            img = Image.open(png_path)
            img.save(webp_path, "WEBP")

            print(f"Converted {png_file} to {os.path.splitext(png_file)[0]}.webp")

            # Delete the original PNG file
            os.remove(png_path)
            print(f"Deleted {png_file}")


# function to get all directories and subdirectories
def listdirs(root_dir):
    # iterate over each directory and check and resize image sizes as needed
    for item in os.scandir(root_dir):
        if item.is_dir():
            listdirs(item)
            convert_images(item.path)


print("⌚️ Converting images this could take a few minutes...")

root = "moonbeam-docs/images/"
listdirs(root)

print(
    "✅ Converting images completed, please check out your local moonbeam-docs directory to see the changes"
)
