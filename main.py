def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_list = count_characters(book_text)
    print_report(book_path, word_count, char_list)


def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()


def count_words(text: str):
    return len(text.split())


def count_characters(text: str):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        elif char.isalpha():
            char_dict[char] = 1
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)


def print_report(book_path: str, word_count: str, char_list: list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in in the document\n")
    for char in char_list:
        print(f"The '{char[0]}' character was found {char[1]} times")
    print("--- End report ---")


main()
