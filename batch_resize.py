# Run this script from a directory that contains images you want to resize. It
# will process all files in the directory. For Python 3, use pillow library
# which is still imported as 'PIL' for some stupid reason.

# This script will overwrite previously generated files if ran multiple times
# in the same directory.

from PIL import Image
from os import listdir


# JPEG export quality
QUALITY = 95


def resize_image(target, scaling_factor):
    # ANTIALIAS will yield the highest quality results at the cost of speed.
    # Other options include: BILINEAR, NEAREST, and BICUBIC
    new_width = target.size[0] * scaling_factor
    new_height = target.size[1] * scaling_factor
    return target.resize([int(new_width), int(new_height)], Image.ANTIALIAS)


def is_picture(file_name):
    flag = False
    extensions = ['.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG']

    for word in extensions:
        if file_name.endswith(word):
            flag = True

    return flag


def main():
    scaling_factor = float(input('Enter scaling factor (10% = 0.1, 200% = 2.0): '))
    file_format = float(input('Select file format: [1]JPEG [2]PNG: '))

    for file_name in listdir('.'):
        if is_picture(file_name):
            img = Image.open(file_name)
            new_img = resize_image(img, scaling_factor)

            if file_format == 1:
                new_img.save(file_name[:-4] + '_resized.jpg', 'JPEG', quality=QUALITY)
            else:
                new_img.save(file_name[:-4] + '_resized.png', 'PNG')

            print('Resized file: ' + file_name)
    print('Script complete.')

if __name__ == "__main__":
    main()
