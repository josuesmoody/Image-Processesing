import sys
import os
from images import read_img, write_img
from transforms import mirror, grayscale, blur, change_colors, rotate, shift, crop, filter

def main():
    if len(sys.argv) < 3 or len(sys.argv) % 2 != 1:
        print("Usage: python transform_multi.py <filename> <transformation1> <args1> <transformation2> <args2> ...")
        return
    
    filename = sys.argv[1]
    transformations = sys.argv[2:]

    try:
        image = read_img(filename)
    except Exception as e:
        print(f"Error al cargar la imagen '{filename}': {e}")
        return

    try:
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
                if i + 1 >= len(transformations):
                    print("Falta argumento para 'change_colors'")
                    return
                original_colors = [tuple(map(int, color.split(','))) for color in transformations[i + 1].split(':')]
                if i + 2 >= len(transformations):
                    print("Falta argumento para 'change_colors'")
                    return
                new_colors = [tuple(map(int, color.split(','))) for color in transformations[i + 2].split(':')]
                transformed_image = change_colors(transformed_image, original_colors, new_colors)
                i += 2
            elif transformation == 'rotate':
                if i + 1 >= len(transformations):
                    print("Falta argumento para 'rotate'")
                    return
                direction = transformations[i + 1]
                transformed_image = rotate(transformed_image, direction)
                i += 1
            elif transformation == 'shift':
                if i + 2 >= len(transformations):
                    print("Faltan argumentos para 'shift'")
                    return
                horizontal = int(transformations[i + 1])
                vertical = int(transformations[i + 2])
                transformed_image = shift(transformed_image, horizontal, vertical)
                i += 3
            elif transformation == 'crop':
                if i + 4 >= len(transformations):
                    print("Faltan argumentos para 'crop'")
                    return
                x = int(transformations[i + 1])
                y = int(transformations[i + 2])
                width = int(transformations[i + 3])
                height = int(transformations[i + 4])
                transformed_image = crop(transformed_image, x, y, width, height)
                i += 4
            elif transformation == 'filter':
                if i + 3 >= len(transformations):
                    print("Faltan argumentos para 'filter'")
                    return
                r = float(transformations[i + 1])
                g = float(transformations[i + 2])
                b = float(transformations[i + 3])
                transformed_image = filter(transformed_image, r, g, b)
                i += 3
            else:
                print(f"Transformación '{transformation}' no reconocida")
                return

            i += 1

        # Carpeta para guardar las imágenes transformadas
        output_dir = 'imagenes_transformadas'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_filename = os.path.join(output_dir, os.path.splitext(os.path.basename(filename))[0] + '_trans_multi.jpg')
        write_img(transformed_image, output_filename)
        print(f"Transformaciones aplicadas con éxito. Imagen guardada en '{output_filename}'")
    except Exception as e:
        print(f"Error al aplicar las transformaciones: {e}")

if __name__ == '__main__':
    main()
