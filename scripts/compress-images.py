from PIL import Image
import os
import sys
import math
import io

root = "moonbeam-docs/images/"

def resize_image(image):
  # Min and Max quality
   Qmin, Qmax = 25, 96
   # Highest acceptable quality found
   Qacc = -1
   while Qmin <= Qmax:
      m = math.floor((Qmin + Qmax) / 2)

      # Encode into memory and get size
      buffer = io.BytesIO()
      image.save(buffer, format="png", quality=m)
      s = buffer.getbuffer().nbytes

      if s <= 921600:
         Qacc = m
         Qmin = m + 1
      elif s > 921600:
         Qmax = m - 1

      
      if Qacc == -1:
        (width, height) = (image.width // 2, image.height // 2)
        image = image.resize((width, height), Image.ANTIALIAS)
        image.save(buffer, format="png", quality=30, optimize=True, compress_level=9)
        print("resized!", buffer.tell()/1024)
        Qacc = 30

      return Qacc

# function to compress images within the given directory
def compress_images(dir):
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
      # check if the image has already been compressed
      if ("compressed-" in image) or ("compressed-" + image in images):
        img = Image.open(image)
        quality = resize_image(img)
        print(os.stat(image).st_size/1000, quality)
        continue
      else:
        # open and compress the image and then save it with a new name
        img = Image.open(image)
        print("Image " + image + " is: " + img.size)
        # img.save("compressed-"+ image, optimize=True, quality=quality)

  # reset directory to mkdocs root
  cwd = os.getcwd()
  mkdocs_root = cwd.split(root)[0]
  os.chdir(mkdocs_root)

# function to get all directories and subdirectories
def listdirs(root_dir):
    # iterate over each directory and compress the images
    for item in os.scandir(root_dir):
        if item.is_dir():
            listdirs(item)
            compress_images(item.path)
    

print("⌚️ Compressing images this could take a few minutes...")
listdirs(root)
print("✅ Compressing images completed")
