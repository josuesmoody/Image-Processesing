from transforms import *
from images import read_img, write_img
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python transforms_simple.py <input_image> <transform>")
        return

    input_filename = sys.argv[1]
    transform = sys.argv[2]

    image = read_img(input_filename)

    if transform == 'mirror':
        transformed_image = mirror(image)
    elif transform == 'grayscale':
        transformed_image = grayscale(image)
    elif transform == 'blur':
        transformed_image = blur(image)
    else:
        print("Transform '{}' not recognized.".format(transform))
        return

    output_filename = input_filename.split('.')[0] + '_trans.png'
    write_img(transformed_image, output_filename)
    print("Transformation '{}' applied successfully. Output saved as '{}'".format(transform, output_filename))

if __name__ == '__main__':
    main()
