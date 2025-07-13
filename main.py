import sys
from stats import word_count, letter_key, sort_on

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    file_path_string = ""
    with open(filepath) as f:
        file_path_string = f.read()
        return file_path_string   
def main():
    book_file = get_book_text(sys.argv[1])
    print(book_file)
      
book_file = get_book_text(sys.argv[1])

# main()
letter_key(book_file)

letter_key_dict = letter_key(book_file)

sorted_stats = sort_on(letter_key_dict)
total_words = word_count(book_file)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")
for entry in sorted_stats:
    print(f"{entry['char']}: {entry['num']}")
print("============= END ===============")