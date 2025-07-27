import sys
from stats import (
    count_words,
    character_counter,
    list_of_dictionaries,
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    
    num_words = count_words(text)
    character_list = character_counter(text)
    list_of_char = list_of_dictionaries(character_list)
    
    print_report(file_path, num_words, list_of_char)


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def print_report(file_path, num_words, list_of_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list_of_char:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()
