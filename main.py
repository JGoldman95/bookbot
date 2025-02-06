def word_count(book):
    # prints the number of words in a file
    words = book.split()
    return len(words)

def char_count(book):
    chars = {}
    for c in book:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def to_list(char_dict):
    transformed = [{"char": char, "num": count} for char, count in char_dict.items()]
    return transformed

def sort_on(dict):
    return dict["num"]

def report(path,words,char_list):
    char_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---")
    if words == 1:
        print(f"{words} word found in the document")
    else:
        print(f"{words} words found in the document")
    print()
    for chara in char_list:
        if chara["char"].isalpha():
            print(f"the \'{chara["char"]}\' character was found {chara["num"]} times")
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = char_count(text)
    chars_list = to_list(chars_dict)
    #print(num_words)
    #print(chars_dict)
    report(book_path, num_words, chars_list)


if __name__ == "__main__":
    main()
