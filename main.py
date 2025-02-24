from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = char_count(text)
    chars_list = to_list(chars_dict)
    #print(num_words)
    print(chars_dict)
    report(book_path, num_words, chars_list)


if __name__ == "__main__":
    main()
