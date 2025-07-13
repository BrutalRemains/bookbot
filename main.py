from stats import word_count, letter_key

def get_book_text(filepath):
    file_path_string = ""
    with open(filepath) as f:
        file_path_string = f.read()
        return file_path_string   
def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    print(frankenstein)


      
frankenstein = get_book_text("books/frankenstein.txt")

# main()
word_count(frankenstein)
letter_key(frankenstein)