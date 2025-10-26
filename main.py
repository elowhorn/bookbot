import sys
from stats import count_words, count_characters, sort_char_counts


def get_book_text(path: str) -> str:
    with open(path) as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    text = get_book_text(path)
    print(f"Analyzing book found at {path}")

    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_count_dict = count_characters(text)
    sorted_count_list = sort_char_counts(char_count_dict)
    print("--------- Character Count -------")
    for char_count in sorted_count_list:
        print(f"{char_count["char"]}: {char_count["num"]}")


main()
