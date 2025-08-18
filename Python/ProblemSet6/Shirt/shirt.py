# Problem Set 6
# Author: Alexis Varas Ortiz
# Program: CS50 P-Shirt
# Description: Overlays the CS50 P-Shirt onto another image
# and saves the result to its own file
import sys
from ntpath import splitext
from PIL import Image, ImageOps


def main():
    try:
        input, output = verify_arguments(sys.argv[1], sys.argv[2])
    # Catch error if there is no second argument
    except IndexError:
        print("Too few command line arguments")
        sys.exit(1)

    overlay_shirt(input, output)
    sys.exit()


#Validate command-line arguments
def verify_arguments(arg1, arg2):
    # Assigning the extensions of the arguments
    ext1 = splitext(arg1.lower())[1]
    ext2 = splitext(arg2.lower())[1]

    # If there are more than 2 arguments display error and exit program
    if len(sys.argv) > 3:
        print("Too many command line arguments")
        sys.exit(1)

    # If the extension for both files don't match display error and exit program
    if ext1 != ext2:
        print("Input and output have different extensions")
        sys.exit(1)

    # If the file extemsion is not a valid image display error and exit program
    if ext1 and ext2 not in (".jpeg", ".jpg", ".png"):
        print("Invalid input")
        sys.exit(1)

    # Return valid arguments
    return arg1, arg2


#Overlay shirt.png over the input image
def overlay_shirt(img_in, img_out):
    try:
        # Open shirt image and input file
        with Image.open("shirt.png") as shirt, Image.open(img_in) as photo:
            photo = ImageOps.fit(photo, shirt.size)  # fit input image to shirt
            photo.paste(shirt, shirt)  # overlay shirt onto input image
            photo.save(img_out)  # save to a new file

    # Catch error if file does not exist or not in the right directory
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    # Back to main()
    return


if __name__ == "__main__":
    main()
