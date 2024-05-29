import os
import images  # Importa el módulo images.py para cargar y guardar imágenes
import transforms  # Importa el módulo transforms.py para aplicar transformaciones a las imágenes

# Verifica si la carpeta 'imagenes_transformadas' existe, si no, la crea
if not os.path.exists('imagenes_transformadas'):
    os.makedirs('imagenes_transformadas')

# Cargar la imagen deseada
imagen_cafe = images.read_img("cafe.jpg")  # Reemplaza "cafe.jpg" con la ruta de tu imagen deseada

# Guardar la imagen original
images.write_img(image=imagen_cafe, filename='imagenes_transformadas/cafe_original.png')  # Cambia el nombre del archivo según sea necesario

# Convertir la imagen a escala de grises y guardarla
grayscale_image = transforms.grayscale(imagen_cafe)
images.write_img(image=grayscale_image, filename='imagenes_transformadas/cafe_grayscale.png')

# Espejar la imagen horizontalmente y guardarla
mirrored_image = transforms.mirror(imagen_cafe)
images.write_img(image=mirrored_image, filename='imagenes_transformadas/cafe_mirrored.png')

# Aplicar desenfoque a la imagen y guardarla
blurred_image = transforms.blur(imagen_cafe)
images.write_img(image=blurred_image, filename='imagenes_transformadas/cafe_blurred.png')

# Cambiar colores de la imagen y guardarla
original_colors = [(255, 0, 0), (0, 0, 255)]
changed_colors = [(0, 255, 0), (255, 255, 0)]
color_changed_image = transforms.change_colors(imagen_cafe, original_colors, changed_colors)
images.write_img(image=color_changed_image, filename='imagenes_transformadas/cafe_color_changed.png')

# Rotar la imagen 90 grados a la derecha y guardarla
rotated_image_right = transforms.rotate(imagen_cafe, 'right')
images.write_img(image=rotated_image_right, filename='imagenes_transformadas/cafe_rotated_right.png')

# Rotar la imagen 90 grados a la izquierda y guardarla
rotated_image_left = transforms.rotate(imagen_cafe, 'left')
images.write_img(image=rotated_image_left, filename='imagenes_transformadas/cafe_rotated_left.png')

# Desplazar la imagen y guardarla
shifted_image = transforms.shift(imagen_cafe, shift_right=10, shift_down=10)
images.write_img(image=shifted_image, filename='imagenes_transformadas/cafe_shifted.png')

print("Transformaciones aplicadas con éxito. Las imágenes transformadas se han guardado en la carpeta 'imagenes_transformadas'.")
