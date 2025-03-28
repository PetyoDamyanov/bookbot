from stats import count_words, count_chars, sort_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    characters = count_chars(text)
    sorted_list = sort_chars(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if char["name"].isalpha():
            print(f"{char["name"]}: {char["num"]}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()