import re
import sys
from spellchecker import SpellChecker

def validate_spelling(file_path):
    print(f"Validating spelling in {file_path}...")

    spell = SpellChecker()

    with open(file_path, "r") as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text)
    misspelled = spell.unknown(words)

    for word in misspelled:
        print(f"Misspelled word: {word}, suggestions: {spell.correction(word)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_spelling.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"No such file: {file_path}")
        sys.exit(1)

    validate_spelling(file_path)