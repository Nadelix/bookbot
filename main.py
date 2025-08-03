import sys
from stats import get_num_words
from stats import count_characters
from stats import sort_chars

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

my_path = sys.argv[1]

with open(my_path) as f:
    text = f.read()

def main():
    num_words = get_num_words(text)
    char_count = count_characters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sort_chars(text)
    print("============= END ===============")


main()