from stats import get_num_words
from stats import get_num_character
from stats import sort_on
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    num_char = {}
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_character(text)
    report = sort_on(num_char)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print ("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print ("--------- Character Count -------")
    for item in report:
        char = item["char"]
        num = item["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {num}")
    print ("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()





main()

