def word_count(book):    
    words = book.split()
    num_words = 0
    for w in words:
        num_words += 1
    print(f"{num_words} words found in the document") 
    return num_words

def letter_key(book):
    letter_key_dict = {}
    
# for each letter/character in the book:
# add the letter to the dictionary

    for letter in book.lower():
        if letter not in letter_key_dict:
            letter_key_dict[letter] = 1
        elif letter in letter_key_dict:
            letter_key_dict[letter] += 1   
        else:
            pass
    
    print(letter_key_dict)
    return letter_key_dict
