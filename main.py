def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = num_of_words(text)
    letter_dict = character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(letter_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_of_words(book):
    word_list = book.split()
    return len(word_list)

def character_count(book):
    lower_text = book.lower()
    character_dict = {}
    for letter in lower_text:
        if letter in character_dict and letter.isalpha():
            character_dict[letter] += 1
        elif letter.isalpha():
            character_dict[letter] = 1
    return character_dict

main()