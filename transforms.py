#Función 
def to_grayscale(image):
    width, height = image['width'], image['height']
    pixels = image['pixels']
    new_pixels = []

    for r, g, b in pixels:
        gray = int((r + g + b) / 3)
        new_pixels.append((gray, gray, gray))

    return {'width': width, 'height': height, 'pixels': new_pixels}

#Función que invierte clores
def invert_colors(image):
    width, height = image['width'], image['height']
    pixels = image['pixels']
    new_pixels = []

    for r, g, b in pixels:
        new_pixels.append((255 - r, 255 - g, 255 - b))

    return {'width': width, 'height': height, 'pixels': new_pixels}
