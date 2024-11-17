import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))


def find_word(letter_soup, word): 
    word = word.upper()
    letter_soup = [[char.upper() for char in row] for row in letter_soup]
    nextTo = [
        (0, 1),   
        (0, -1),  
        (1, 0),   
        (-1, 0),  
        (1, 1),   
        (-1, -1), 
        (1, -1),  
        (-1, 1)   
    ]
    
    rows, cols = len(letter_soup), len(letter_soup[0])
    for i in range(rows):
        for j in range(cols):
            if letter_soup[i][j] == word[0]:
                for posx, posy in nextTo:
                    if all(
                        0 <= i + k * posx < rows and
                        0 <= j + k * posy < cols and
                        letter_soup[i + k * posx][j + k * posy] == word[k]
                        for k in range(len(word))
                    ):
                        return True
    return False

def find_words(letter_soup, words):
    """Encuentra todas las palabras en la sopa de letras."""
    results = {}
    for word in words:
        results[word] = find_word(letter_soup, word)
    return results