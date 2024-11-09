def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    words = number_of_words(book)
    characters = characters_appear(book)
    character_occurances = print_character_appearences(characters)
    print(f"There are {words} words in the document.")
    for item in character_occurances:
        print(f"The {item['char']} character was found {item['num']} times.")
    
def print_character_appearences(dictionary):
    list_of_dicts = []
    for key in dictionary:
        if key.isalpha():
            new_dict = {"char": key, "num": dictionary[key]}
            list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def get_book_text(path):
    with open(path, "r") as f:
        file_contents = f.read()
    return file_contents

def number_of_words(text):
    words = text.split()
    return len(words)

def characters_appear(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]


main()
        
