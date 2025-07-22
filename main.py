import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import get_num_words
from stats import count_characters
from stats import sortare

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    contents = get_book_text(sys.argv[1])

    return contents

text = main()
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f'Found {get_num_words(text)} total words')
print("---------- Character Count -------")
sortare(text)
print("============= END ===============")