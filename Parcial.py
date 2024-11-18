import json
# Función para buscar una palabra en la sopa de letras
def find_word(letter_soup, word):
    word = word.lower()  # Convertir la palabra a minúsculas para hacer la búsqueda insensible a mayúsculas
    for row in range(len(letter_soup)):
        for col in range(len(letter_soup[row])):
            # Buscar la palabra en las 8 direcciones posibles (horizontal, vertical, diagonal)
            if (search_in_direction(letter_soup, word, row, col, 0, 1) or  # Horizontal derecha
                search_in_direction(letter_soup, word, row, col, 1, 0) or  # Vertical abajo
                search_in_direction(letter_soup, word, row, col, 1, 1) or  # Diagonal abajo derecha
                search_in_direction(letter_soup, word, row, col, 1, -1) or # Diagonal abajo izquierda
                search_in_direction(letter_soup, word, row, col, 0, -1) or # Horizontal izquierda
                search_in_direction(letter_soup, word, row, col, -1, 0) or # Vertical arriba
                search_in_direction(letter_soup, word, row, col, -1, -1) or# Diagonal arriba izquierda
                search_in_direction(letter_soup, word, row, col, -1, 1)): # Diagonal arriba derecha
                return True
    return False

def search_in_direction(letter_soup, word, row, col, row_dir, col_dir):
    length = len(word)
    if row + row_dir * (length - 1) < 0 or row + row_dir * (length - 1) >= len(letter_soup):
        return False
    if col + col_dir * (length - 1) < 0 or col + col_dir * (length - 1) >= len(letter_soup[0]):
        return False

    for i in range(length):
        if letter_soup[row + i * row_dir][col + i * col_dir].lower() != word[i]:
            return False
    return True  


def find_words(letter_soup, words):
    result = {}
    for word in words:
        result[word] = find_word(letter_soup, word)
    return result

# Función para generar el reporte en formato JSON
def generate_report(output_path, letter_soup, words):
    result = find_words(letter_soup, words)
    
    # Crear un diccionario con los resultados
    report = result
    
    
    # Escribir el reporte en un archivo JSON
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"Reporte generado en: {output_path}")

# Función para obtener el contenido del archivo
def get_file_content(file_path):
    with open(file_path, 'r') as f:
        content = f.read().splitlines()

    # Separar la sopa de letras y las palabras a buscar
    letter_soup = []
    words = []
    reading_words = False

    for line in content:
        if line == '--':
            reading_words = True
            continue
        if not reading_words:
            letter_soup.append(line)
        else:
            words.append(line)
    
    return letter_soup, words

# Cambia 'ruta/al/archivo.txt' por la ruta completa o simplemente 'archivo.txt' si está en la misma carpeta
file_path = 'C:\\Users\\Principal\\Documents\\JAVE\\PARCIAL\\archivo.txt'
letter_soup, words = get_file_content(file_path)
print("Sopa de letras:", letter_soup)
print("Palabras a buscar:", words)

# Ejecución principal
file_path = 'archivo.txt'
output_path = 'C:\\Users\\Principal\\Documents\\JAVE\\PARCIAL\\archivo_salida.json'
generate_report(output_path, letter_soup, words)