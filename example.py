import images  # Importa el módulo images.py para cargar y guardar imágenes
import transforms  # Importa el módulo transforms.py para aplicar transformaciones a las imágenes

"""Rectángulo de tres por dos píxeles, con los colores rojo (los dos píxeles de arriba)
y azul (los dos píxeles de abajo)
"""
# Imagen original
imagen = images.read_img("cafe.jpg")

# Convertir la imagen a escala de grises y guardarla
grayscale_image = transforms.grayscale(imagen)
images.write_img(image=grayscale_image, filename='cafe_grayscale.jpg')

# Espejar la imagen horizontalmente y guardarla
mirrored_image = transforms.mirror(imagen)
images.write_img(image=mirrored_image, filename='cafe_mirrored.jpg')
