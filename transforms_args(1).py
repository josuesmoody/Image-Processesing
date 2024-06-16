import sys
import os
from images import read_img, write_img
from transforms import * # mirror, grayscale, blur, change_colors, rotate, shift, crop, filter

def valores():
    if len(sys.argv) < 3:
        raise ValueError("Uso: python transform_args.py <filename> <transform> [<args>...]")
    input_filename = sys.argv[1]
    transform = sys.argv[2]
    return input_filename, transform

def main():
    try:
        nombre_original, cambios = valores()
        image = read_img(nombre_original)

        if cambios == 'mirror':
            transformed_image = mirror(image)
        elif cambios == 'grayscale':
            transformed_image = grayscale(image)
        elif cambios == 'blur':
            transformed_image = blur(image)
        elif cambios == 'change_colors': # tiene 6 parametros
            if len(sys.argv) < 5:
                print("Uso: python transform_args.py <filename> change_colors <original_colors> <new_colors>")
                return

            # Convertir los colores originales de la cadena a tuplas
            original_colors = []
            for color in sys.argv[3].split(':'):
                r, g, b = color.split(',')
                original_colors.append((int(r), int(g), int(b)))

            # Convertir los nuevos colores de la cadena a tuplas
            new_colors = []
            for color in sys.argv[4].split(':'):
                r, g, b = color.split(',')
                new_colors.append((int(r), int(g), int(b)))

            transformed_image = change_colors(image, original_colors, new_colors)
        elif cambios == 'rotate':
            if len(sys.argv) < 4:
                print("Uso: python transform_args.py <filename> rotate <direction>")
                return
            direction = sys.argv[3]
            transformed_image = rotate(image, direction)
        elif cambios == 'shift':
            if len(sys.argv) < 5:
                print("Uso: python transform_args.py <filename> shift <horizontal> <vertical>")
                return
            horizontal = int(sys.argv[3])
            vertical = int(sys.argv[4])
            transformed_image = shift(image, horizontal, vertical)
        elif cambios == 'crop':
            if len(sys.argv) < 7:
                print("Uso: python transform_args.py <filename> crop <x> <y> <width> <height>")
                return
            x = int(sys.argv[3])
            y = int(sys.argv[4])
            width = int(sys.argv[5])
            height = int(sys.argv[6])
            transformed_image = crop(image, x, y, width, height)
        elif cambios == 'filter':
            if len(sys.argv) < 6:
                print("Uso: python transform_args.py <filename> filter <r> <g> <b>")
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

        output_filename = os.path.join(output_dir, os.path.splitext(os.path.basename(nombre_original))[0] + '_trans.png')
        write_img(transformed_image, output_filename)
        print(f"Transformación '{cambios}' aplicada con éxito. Imagen guardada en '{output_filename}'")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Error al aplicar la transformación: {e}")

if __name__ == '__main__':
    main()
