import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from word_search import find_words

def generate_report(letter_soup, words, output_path="output.json"):
    """Genera un archivo JSON con el reporte de palabras encontradas."""
    report = find_words(letter_soup, words)
    with open(output_path, "w") as f:
        json.dump(report, f, indent=4)