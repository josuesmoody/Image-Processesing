import sys
import os
from images import read_img, write_img
from transforms import * #mirror, grayscale, blur, change_colors, rotate, shift, crop, filter

def valores():
    input_filename = sys.argv[1]
    transform = sys.argv[2]
    return input_filename, transform

def main():
    nombre_original, cambios = valores()
    image = read_img(nombre_original)

    if image == 'mirror':
        image = mirror(image)
    elif image == 'grayscale':
        transformed_image = grayscale(image)
    elif image == 'blur':
        transformed_image = blur(image)

    elif image == 'change_colors': #tiene 6 parametros
        #color.append(int(r), int(g), int(b))
        color = (int("r"), int("g"), int("b"))
        original_colors = (color.split(',')) for color in sys.argv[3].split(':')
        original_colors = color
        new_colors = [tuple(int())]
        new_colors = [tuple(int(color.split(',')) for color in sys.argv[4].split(':')]
        image = change_colors(image, original_colors, new_colors)

    elif image == 'rotate':
        direction = sys.argv[3]
        transformed_image = rotate(image, direction)

    elif image == 'shift':
            if len(sys.argv) < 5:
                print("Uso: python transform_args.py <filename> shift <horizontal> <vertical>")
                return
            horizontal = int(sys.argv[3])
            vertical = int(sys.argv[4])
            transformed_image = shift(image, horizontal, vertical)
        elif image == 'crop':
            if len(sys.argv) < 7:
                print("Uso: python transform_args.py <filename> crop <x> <y> <width> <height>")
                return
            x = int(sys.argv[3])
            y = int(sys.argv[4])
            width = int(sys.argv[5])
            height = int(sys.argv[6])
            transformed_image = crop(image, x, y, width, height)
        elif image == 'filter':
            if len(sys.argv) < 6:
                print("Usage: python transform_args.py <filename> filter <r> <g> <b>")
                return
            r = float(sys.argv[3])
            g = float(sys.argv[4])
            b = float(sys.argv[5])
            transformed_image = filter(image, r, g, b)
        else:
            print("Transformación no reconocida")
            return

        # Carpeta para guardar las imágenes transformadas
        output_dir = 'imagenes_transformadas'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_filename = os.path.join(output_dir, os.path.splitext(os.path.basename(filename))[0] + '_trans.png')
        write_img(transformed_image, output_filename)
        print(f"Transformación '{transformation}' aplicada con éxito. Imagen guardada en '{output_filename}'")
    except Exception as e:
        print(f"Error al aplicar la transformación '{transformation}': {e}")


if __name__ == '__main__':
    main()