# ------- 👋 Welcome to the script for compressing images ------- #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to compress images that are       #
# larger than 900KB.                                              #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` repo is      #
# nestled inside of the `moonbeam-mkdocs` repo. Then simply run   #
# `python scripts/compress-images.py` in your terminal. The       #
# script will check all of the images to see the current size and #
# if any are larger than 900KB, it will use the Tinify library to #
# compress the images. Tinify compresses images by selectively    #
# decreasing the number of colors in the image so fewer bytes are #
# required to store the data. To use the Tinify library, you will #
# need an API key. Check LastPass or create your own using the    #
# link below. Once compression is done, you will see that the     #
# original image has been replaced. If the image happens to be    #
# the same size or larger after compression, you will be notified #
# to manually resize the image in Inkscape and re-run the script. #
# Once the script is complete, you can commit the changes in your #
# local `moonbeam-docs` repo! And that's it!                      #

import os
import tinify
from PIL.PngImagePlugin import PngImageFile, PngInfo

# https://tinypng.com/developers
tinify.key = "INSERT_API_KEY_HERE"

# function to resize large images
def compress_image(image, original_size):
    print("🖼 Compressing " + image)

    # compress the image
    compressed_image = tinify.from_file(image)
        
    # save to file
    compressed_image.to_file(image)

    # check the image size, if the image hasn't gone down in size, try resizing in inkscape
    size_in_kilobytes = os.stat(image).st_size/1024
    if size_in_kilobytes >= original_size:
        print("Image increased in size after compression, please resize this image manually in Inkscape and run the script again (" + image + ")")
        print("==========")
    else:
        # use metadata to mark the file as compressed
        img = PngImageFile(image)
        metadata = PngInfo()
        metadata.add_text("compressed", "true")
        img.save(image, pnginfo=metadata)

# function to check image size and determine if compression is needed
def check_size(dir):
    # change the directory
    os.chdir(dir)
    files = os.listdir()

    # extract all of the images:
    images = [file for file in files if file.endswith(('png'))]

    # some directories may only contain subdirectories without images to compress, so make sure
    # there are images that can be compressed before proceeding
    if len(images) > 0:
        # iterate over each of the images
        for image in images:
            # represents the size of the file in bytes
            size_in_bytes = os.stat(image).st_size
            size_in_kilobytes = size_in_bytes/1024

            img = PngImageFile(image)

            # check if size of the image is larger than 900KB
            if size_in_kilobytes > 900:
                # check metadata to see if image has already been compressed
                if "compressed" not in img.text:
                    compress_image(image, size_in_kilobytes)

    # reset directory to mkdocs root
    cwd = os.getcwd()
    mkdocs_root = cwd.split(root)[0]
    os.chdir(mkdocs_root)

# function to get all directories and subdirectories
def listdirs(root_dir):
    # iterate over each directory and check and resize image sizes as needed
    for item in os.scandir(root_dir):
        if item.is_dir():
            listdirs(item)
            check_size(item.path)

print("⌚️ Compressing images this could take a few minutes...")

root = "moonbeam-docs/images/"
listdirs(root)

print("✅ Compressing images completed, please check out your local moonbeam-docs directory to see the changes")
