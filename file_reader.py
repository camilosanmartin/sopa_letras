def get_file_content(file_path):
    """Lee el contenido de un archivo y lo devuelve como una lista de líneas."""
    with open(file_path) as f:
        content = f.read().splitlines()
    return content