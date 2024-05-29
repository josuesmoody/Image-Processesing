import sys
from images import read_img, write_img
from transforms import mirror, grayscale, blur, change_colors, rotate, shift, crop, filter

def main():
    if len(sys.argv) < 3:
        print("Usage: python transform_multi.py <filename> <transformation1> <args1> <transformation2> <args2> ...")
        return

    filename = sys.argv[1]
    image = read_img(filename)

    transformations = sys.argv[2:]
    transformed_image = image

    i = 0
    while i < len(transformations):
        transformation = transformations[i]
        if transformation == 'mirror':
            transformed_image = mirror(transformed_image)
        elif transformation == 'grayscale':
            transformed_image = grayscale(transformed_image)
        elif transformation == 'blur':
            transformed_image = blur(transformed_image)
        elif transformation == 'change_colors':
            if len(transformations) < i + 3:
                print("Usage: python transform_multi.py <filename> change_colors <original_colors> <new_colors>")
                return
            original_colors = [tuple(map(int, color.split(','))) for color in transformations[i+1].split(':')]
            new_colors = [tuple(map(int, color.split(','))) for color in transformations[i+2].split(':')]
            transformed_image = change_colors(transformed_image, original_colors, new_colors)
            i += 2  # Skip next two elements
        elif transformation == 'rotate':
            if len(transformations) < i + 2:
                print("Usage: python transform_multi.py <filename> rotate <direction>")
                return
            direction = transformations[i+1]
            transformed_image = rotate(transformed_image, direction)
            i += 1  # Skip next element
        elif transformation == 'shift':
            if len(transformations) < i + 3:
                print("Usage: python transform_multi.py <filename> shift <horizontal> <vertical>")
                return
            horizontal = int(transformations[i+1])
            vertical = int(transformations[i+2])
            transformed_image = shift(transformed_image, horizontal, vertical)
            i += 2  # Skip next two elements
        elif transformation == 'crop':
            if len(transformations) < i + 5:
                print("Usage: python transform_multi.py <filename> crop <x> <y> <width> <height>")
                return
            x = int(transformations[i+1])
            y = int(transformations[i+2])
            width = int(transformations[i+3])
            height = int(transformations[i+4])
            transformed_image = crop(transformed_image, x, y, width, height)
            i += 4  # Skip next four elements
        elif transformation == 'filter':
            if len(transformations) < i + 4:
                print("Usage: python transform_multi.py <filename> filter <r> <g> <b>")
                return
            r = float(transformations[i+1])
            g = float(transformations[i+2])
            b = float(transformations[i+3])
            transformed_image = filter(transformed_image, r, g, b)
            i += 3  # Skip next three elements
        else:
            print("Transformation not recognized:", transformation)
            return

        i += 1  # Move to the next transformation

    write_img(transformed_image, filename.split('.')[0] + '_trans.png')

if __name__ == '__main__':
    main()
