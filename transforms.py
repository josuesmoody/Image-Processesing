# transforms.py

def mirror(image: dict) -> dict:
    """
    Espeja la imagen según un eje horizontal situado en la mitad de la imagen.
    """
    width, height = image['width'], image['height']
    pixels = image['pixels']
    new_pixels = pixels.copy()

    for y in range(height // 2):
        for x in range(width):
            top_index = y * width + x
            bottom_index = (height - y - 1) * width + x
            new_pixels[top_index], new_pixels[bottom_index] = pixels[bottom_index], pixels[top_index]

    return {'width': width, 'height': height, 'pixels': new_pixels}

def grayscale(image: dict) -> dict:
    """
    Convierte la imagen a escala de grises.
    """
    width, height = image['width'], image['height']
    pixels = image['pixels']
    new_pixels = []

    for r, g, b in pixels:
        gray = int((r + g + b) / 3)
        new_pixels.append((gray, gray, gray))

    return {'width': width, 'height': height, 'pixels': new_pixels}
