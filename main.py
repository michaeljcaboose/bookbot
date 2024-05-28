def main():   
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of ${book_path} ---")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    letters = count_letters(text)
    letter_quantities = convert_to_list(letters) 
    letter_quantities.sort(reverse=True, key=sort_on_quantity)
    
    for l in letter_quantities:
        print(f"The '{l["name"]}' character was found {l["quantity"]} times")

    print("--- End Report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def convert_to_list(dict):
    letters = []
    for l in dict:
        letters.append({"name": l, "quantity": dict[l]})
    return letters

def sort_on_quantity(dict):
    return dict["quantity"]
    
main()