import os
from images import read_img, write_img
from transforms import mirror

def main():
    filename = "cafe.jpg"  # Nombre del archivo de entrada
    transformation = "mirror"  # Transformación a aplicar

    try:
        image = read_img(filename)
    except Exception as e:
        print(f"Error al cargar la imagen '{filename}': {e}")
        return

    try:
        if transformation == 'mirror':
            transformed_image = mirror(image)
        else:
            print("Transformación no reconocida")
            return

        # Carpeta para guardar las imágenes transformadas
        output_dir = 'imagenes_transformadas'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_filename = os.path.join(output_dir, os.path.basename(filename).split('.')[0] + '_trans_args.png')
        write_img(transformed_image, output_filename)
        print(f"Transformación '{transformation}' aplicada con éxito. Imagen guardada en '{output_filename}'")
    except Exception as e:
        print(f"Error al aplicar la transformación '{transformation}': {e}")

if __name__ == '__main__':
    main()
