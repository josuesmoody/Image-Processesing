import sys
from images import read_img, write_img  # Añadir esta línea para importar read_img y write_img de images.py
from transforms import mirror, grayscale, blur, change_colors, rotate, shift, crop, filter

def main():
    if len(sys.argv) < 3:
        print("Usage: python transform_args.py <filename> <transformation>")
        return
    
    filename = sys.argv[1]
    transformation = sys.argv[2]

    image = read_img(filename)  # Usar read_img del módulo images

    if transformation == 'mirror':
        transformed_image = mirror(image)
    elif transformation == 'grayscale':
        transformed_image = grayscale(image)
    elif transformation == 'blur':
        transformed_image = blur(image)
    elif transformation == 'change_colors':
        if len(sys.argv) < 5:
            print("Usage: python transform_args.py <filename> change_colors <original_colors> <new_colors>")
            return
        original_colors = [tuple(map(int, color.split(','))) for color in sys.argv[3].split(':')]
        new_colors = [tuple(map(int, color.split(','))) for color in sys.argv[4].split(':')]
        transformed_image = change_colors(image, original_colors, new_colors)
    elif transformation == 'rotate':
        if len(sys.argv) < 4:
            print("Usage: python transform_args.py <filename> rotate <direction>")
            return
        direction = sys.argv[3]
        transformed_image = rotate(image, direction)
    elif transformation == 'shift':
        if len(sys.argv) < 5:
            print("Usage: python transform_args.py <filename> shift <horizontal> <vertical>")
            return
        horizontal = int(sys.argv[3])
        vertical = int(sys.argv[4])
        transformed_image = shift(image, horizontal, vertical)
    elif transformation == 'crop':
        if len(sys.argv) < 7:
            print("Usage: python transform_args.py <filename> crop <x> <y> <width> <height>")
            return
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        width = int(sys.argv[5])
        height = int(sys.argv[6])
        transformed_image = crop(image, x, y, width, height)
    elif transformation == 'filter':
        if len(sys.argv) < 6:
            print("Usage: python transform_args.py <filename> filter <r> <g> <b>")
            return
        r = float(sys.argv[3])
        g = float(sys.argv[4])
        b = float(sys.argv[5])
        transformed_image = filter(image, r, g, b)
    else:
        print("Transformation not recognized")
        return

    write_img(transformed_image, filename.split('.')[0] + '_trans.png')  # Usar write_img del módulo images

if __name__ == '__main__':
    main()
