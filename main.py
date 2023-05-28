# Convert all images in a folder to PDF
import os
import re
import sys

from heic2png import HEIC2PNG
from PIL import Image

def main(argv) -> int:
    """
    Convert all images in a folder to PDF
    arg[1]: Filepath to directory with images
    """
    if len(argv) < 2:
        print("Did you specify a filepath?")
        return 1 
    if len(argv) >= 3:
        print("Error. Too many arguments provided. Only specify one filepath")
        return 2
    # get file path from argv user input
    file_path = argv[1]
    # get a list of the files in the directory
    files = os.listdir(file_path)
    # check for heic files. If found, convert to PNG
    for file in files:
        if re.match("(.*\.HEIC$)|(.*\.heic$)", file):
            heic_img_filepath = os.path.join(file_path, file)
            heic_img = HEIC2PNG(heic_img_filepath)
            heic_img.save()

    # sort the list after rereading
    files = [file for file in os.listdir(file_path) if re.search("^($\.)|.*\.png$", file)]
    files = sorted(files)
    # create list to hold the images that will be appended
    img_list = []
    # open each file convert to PDF and append 
    for i, file in enumerate(files):
        print(f"\nConverting file number {i} to -> {file}.")
        img = Image.open(os.path.join(file_path, file)).convert("RGB")
        img_list.append(img)
    # Append images together
    img_list[0].save(
        os.path.join(file_path, "combined.pdf"), 
        "PDF", 
        save_all=True, 
        append_images=img_list[1:]
    )

    print(f"\nFile converted to PDF and combined successfully.")
    return 0

if __name__ == "__main__":
    main(sys.argv)
