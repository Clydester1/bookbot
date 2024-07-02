def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    characters = character_count(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    sorting(characters)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    word = text.split()
    return len(word)

def character_count(text):
    word = text.lower()
    my_dict = {}
    for i in word:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
    return my_dict

def sort_on(dict):
    return dict["num"]

def sorting(characters):
    lis = []

    for i in characters:
        if i.isalpha() == True:
            lis.append({"character": i, "num": characters[i]})
    lis.sort(reverse=True, key=sort_on)

    for b in range(len(lis)):
        c = lis[b]["character"]
        d = lis[b]["num"]
        print(f"The '{c}' character was found '{d}' times")



main()