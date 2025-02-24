def get_num_words(book):
    #prints the number of words in a file
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
    transformed = [{char: count} for char, count in char_dict.items()]
    return transformed

def sort_on(dict):
    return list(dict.values())[0]

def report(path,words,char_list):
    char_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    if words == 1:
        print(f"Found {words} total word")
    else:
        print(f"Found {words} total words")
    print()
    for char_dict in char_list:
        char = list(char_dict.keys())[0]
        count = list(char_dict.values())[0]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")