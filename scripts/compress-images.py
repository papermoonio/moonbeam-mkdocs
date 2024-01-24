# ------- 👋 Welcome to the script for compressing images ------- #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# The purpose of this script is to compress images that are       #
# larger than 900KB.                                              #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# To use the script, ensure that the `moonbeam-docs` repo is      #
# nestled inside of the `moonbeam-mkdocs` repo. Then simply run   #
# `python scripts/compress-images.py` in your terminal. The       #
# script will check all of the images to see the current size and #
# if any are larger than 900KB, it will compress the images. If   #
# the image happens to be the same size or larger after           #
# compression, you will be notified to manually resize the image  #
# in Inkscape and re-run the script. Once the script is complete, #
# you can commit the changes in your local `moonbeam-docs` repo!  #
# And that's it!                                                  #

from PIL import Image
import os


def compress_large_webp_images(input_dir):
    for webp_file in os.listdir(input_dir):
        if webp_file.lower().endswith(".webp"):
            # Get the full file path
            webp_path = os.path.join(input_dir, webp_file)

            # Get the size of the image in bytes
            size_in_bytes = os.stat(webp_path).st_size

            # Convert size to kilobytes
            size_in_kilobytes = size_in_bytes / 1024

            # Check if the image size is greater than 900KB
            if size_in_kilobytes > 900:
                # Open the WebP image
                img = Image.open(webp_path)
                metadata = img.info

                if "compressed" not in metadata:
                    # Compress the image
                    img.save(webp_path, "WEBP", quality=80)  # Adjust quality as needed

                    # Get the new size of the compressed image
                    new_size_in_bytes = os.stat(webp_path).st_size
                    new_size_in_kilobytes = new_size_in_bytes / 1024

                    if new_size_in_kilobytes >= size_in_kilobytes:
                        print(
                            "Image increased in size after compression, please re-export this image manually using a lower dpi in Inkscape and run the script again ("
                            + webp_path
                            + ")"
                        )
                        print("==========")
                    else:
                        # use metadata to mark the file as compressed
                        img = Image.open(webp_path)
                        metadata = img.info.copy()
                        metadata["compressed"] = "true"

                        # Save the WebP image with the added metadata
                        img.save(webp_path, "WEBP", pnginfo=metadata)

                        print(
                            f"Compressed {webp_file}: {size_in_kilobytes:.2f}KB -> {new_size_in_kilobytes:.2f}KB"
                        )


# function to get all directories and subdirectories
def listdirs(root_dir):
    # iterate over each directory and check and resize image sizes as needed
    for item in os.scandir(root_dir):
        if item.is_dir():
            listdirs(item)
            compress_large_webp_images(item.path)


print("⌚️ Compressing images this could take a few minutes...")

root = "moonbeam-docs/images/"
listdirs(root)

print(
    "✅ Compressing images completed, please check out your local moonbeam-docs directory to see the changes"
)
