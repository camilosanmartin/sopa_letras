from file_reader import get_file_content
from json_generator import generate_report

def main():
    file_path = "sopa.txt"
    content = get_file_content(file_path)
    
    # Esta linea se usa para separar en el contenido de las primeras 5 lineas del .txt donde supuestamente debería de estar la sopa de letras pasada por el usuario
    letter_soup = [list(row) for row in content[:5]] 
#creando un arreglo para una lista de filas donde contiene cada una de las filas de la sopa de letras hasta la 5 linea
    #Se comienza a leer desde la linea 6 "saltando las 3 barras medias dejadas en el .txt" para ver las palabras
    words = content[6:]
#lee las palabras y las guarda        
    generate_report(letter_soup, words)

if __name__ == "__main__": #invoca funcion main como objeto 
    main()
