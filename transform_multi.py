import os
import images
import transforms

def main():
    filename = "cafe.jpg"  # Nombre de la imagen de entrada

    if not os.path.exists('imagenes_transformadas'):
        os.makedirs('imagenes_transformadas')

    try:
        image = images.read_img(filename)
    except Exception as e:
        print(f"Error al cargar la imagen '{filename}': {e}")
        return

    try:
        # Aplicar transformaciones
        image = transforms.grayscale(image)
        print("Transformación 'grayscale' aplicada con éxito.")
        
        image = transforms.mirror(image)
        print("Transformación 'mirror' aplicada con éxito.")
        
        image = transforms.blur(image)
        print("Transformación 'blur' aplicada con éxito.")
    except Exception as e:
        print(f"Error al aplicar transformaciones: {e}")
        return

    try:
        output_file = os.path.join('imagenes_transformadas', 'cafe_trans_multi.jpg')
        images.write_img(image, output_file)
        print(f"Imagen transformada guardada en '{output_file}'")
    except Exception as e:
        print(f"Error al guardar la imagen transformada: {e}")

if __name__ == "__main__":
    main()
