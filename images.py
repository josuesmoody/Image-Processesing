from PIL import Image

"""Módulo para manejar imágenes

Las imágenes en este módulo se manejan como diccionarios, con tres claves:
  * width: ancho de la imagen, en pixels
  * height: alto de la imagen, en pixels
  * pixels: lista de pixels de la imagen (longitud: width * height)
Cada pixel de la image será una tupla, con valores para cada color
RGB (rojo, verde, azul). Cada color será un número entero.
"""

def size(image: dict) -> tuple[int, int]:
    """Devuelve el tamaño de una imagen, dado un diccionario con una imagen.
    Devuelve una tupla (width, height).
    """
    width = image['width']
    height = image['height']
    return (width, height)

def read_img(filename: str) -> dict:
    """Lee una imagen de un fichero, y devuelve una imagen como diccionario"""
    img = Image.open(filename)
    image = {}
    image['width'], image['height'] = img.size
    image['pixels'] = list(img.getdata())
    return image

def write_img(image: dict, filename: str) -> None:
    """Escribe una imagen (diccionario) en un fichero"""
    (width, height) = size(image)
    img = Image.new(mode='RGB', size=(width, height))
    img.putdata(image['pixels'])
    img.save(filename)

def create_blank(width: int, height: int) -> dict:
    """Crea una imagen (diccionario) vacía, dada una anchura y una altura."""
    image = {}
    image['width'], image['height'] = width, height
    image['pixels'] = [(0, 0, 0)] * (height * width)
    return image
