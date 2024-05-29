from images import create_blank, size

# Espeja la imagen horizontalmente
def mirror(image: dict) -> dict:
    width, height = size(image)
    mirrored_image = create_blank(width, height)
    for y in range(height):
        for x in range(width):
            mirrored_image['pixels'][x + width * y] = image['pixels'][x + width * (height - 1 - y)]
    return mirrored_image

# Convierte la imagen a escala de grises
def grayscale(image: dict) -> dict:
    width, height = size(image)
    grayscale_image = create_blank(width, height)
    for y in range(height):
        for x in range(width):
            r, g, b = image['pixels'][x + width * y]
            gray = (r + g + b) // 3
            grayscale_image['pixels'][x + width * y] = (gray, gray, gray)
    return grayscale_image

# Aplica un efecto de desenfoque a la imagen
def blur(image: dict) -> dict:
    width, height = size(image)
    blurred_image = create_blank(width, height)
    for y in range(height):
        for x in range(width):
            reds, greens, blues = [], [], []
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        r, g, b = image['pixels'][nx + width * ny]
                        reds.append(r)
                        greens.append(g)
                        blues.append(b)
            blurred_image['pixels'][x + width * y] = (
                sum(reds) // len(reds),
                sum(greens) // len(greens),
                sum(blues) // len(blues)
            )
    return blurred_image

# Cambia los colores de la imagen según las listas de colores proporcionadas
def change_colors(image: dict, original: list[tuple[int, int, int]], change: list[tuple[int, int, int]]) -> dict:
    width, height = size(image)
    new_image = create_blank(width, height)
    color_map = {orig: chng for orig, chng in zip(original, change)}
    for y in range(height):
        for x in range(width):
            pixel = image['pixels'][x + width * y]
            new_image['pixels'][x + width * y] = color_map.get(pixel, pixel)
    return new_image

# Gira la imagen 90 grados a la izquierda o a la derecha
def rotate(image: dict, direction: str) -> dict:
    width, height = size(image)
    rotated_image = create_blank(height, width)  # Rotated image will have swapped width and height
    for y in range(height):
        for x in range(width):
            if direction == 'right':
                rotated_image['pixels'][y + height * (width - 1 - x)] = image['pixels'][x + width * y]
            elif direction == 'left':
                rotated_image['pixels'][(height - 1 - y) + height * x] = image['pixels'][x + width * y]
    return rotated_image

# Desplaza la imagen en el eje horizontal y/o vertical según se indique
def shift(image: dict, shift_right: int = 0, shift_down: int = 0) -> dict:
    width, height = size(image)
    new_width, new_height = width + shift_right, height + shift_down
    shifted_image = create_blank(new_width, new_height)
    for y in range(height):
        for x in range(width):
            new_x, new_y = x + shift_right, y + shift_down
            if 0 <= new_x < new_width and 0 <= new_y < new_height:
                shifted_image['pixels'][new_x + new_width * new_y] = image['pixels'][x + width * y]
    return shifted_image

# Crea una nueva imagen que contiene solo los píxeles dentro del rectángulo especificado.
def crop(image: dict, x: int, y: int, width: int, height: int) -> dict:

    cropped_pixels = []
    original_width = image['width']
    original_height = image['height']
    
    for dy in range(height):
        for dx in range(width):
            if 0 <= x + dx < original_width and 0 <= y + dy < original_height:
                cropped_pixels.append(image['pixels'][(x + dx) + (y + dy) * original_width])
    
    return {'width': width, 'height': height, 'pixels': cropped_pixels}

# Crea una nueva imagen con un filtro aplicado a todos sus píxeles.
def filter(image: dict, r: float, g: float, b: float) -> dict:

    filtered_pixels = []
    
    for pixel in image['pixels']:
        filtered_pixel = tuple(min(int(component * multiplier), 255) for component, multiplier in zip(pixel, (r, g, b)))
        filtered_pixels.append(filtered_pixel)
    
    return {'width': image['width'], 'height': image['height'], 'pixels': filtered_pixels}
