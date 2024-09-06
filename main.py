def get_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_number_words(text):
    words = text.split()
    return len(words)

def get_character_ammounts(text):
    characters = {}
    text = text.lower()
    for c in text.lower():
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def dictionary_to_list(dictionary):
    dict_list = []
    for d in dictionary:
        dict_list.append({"name": d, "num": dictionary[d]})
    return dict_list

def sort_ammount(dictionary):
    return dictionary["num"]

def print_info(text):
    print("--- Begin report of books/frankenstein.txt ---")
    
    word_count = get_number_words(text)
    print(word_count, " words found in the document \n")
    
    character_count = get_character_ammounts(text)
    character_list = dictionary_to_list(character_count)
    character_list.sort(reverse=True, key=sort_ammount)
    for item in character_list:
        if item["name"].isalpha():
            print("The ", item["name"], "character was found ", item["num"], " times")


text = get_text("books/frankenstein.txt")
print_info(text)