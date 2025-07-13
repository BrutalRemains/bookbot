def word_count(book):    
    words = book.split()
    num_words = 0
    for w in words:
        num_words += 1
    
    return num_words

def letter_key(book):
    letter_key_dict = {}
    
    for letter in book.lower():
        if letter not in letter_key_dict:
            letter_key_dict[letter] = 1
        elif letter in letter_key_dict:
            letter_key_dict[letter] += 1   
        else:
            pass
    
    
    return letter_key_dict

def sort_on(dictionary):
    printed_report = []
    

    for key, value in dictionary.items():
        if key.isalpha():
            new_dict = {"char": key,
                    "num": value}
            printed_report.append(new_dict)
    
    printed_report.sort(reverse=True, key=lambda item: item["num"])
    return printed_report
         
    
    