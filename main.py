from stats import get_num_words, get_char_count, format_count
import sys
def get_book_text(filepath):
    with open (filepath) as f:
        file_contents=f.read()
        return file_contents


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    num_words=get_num_words(get_book_text(sys.argv[1]))
    char_count=get_char_count(get_book_text(sys.argv[1]))
    print(f"Found {num_words} total words")  
    print("--------- Character Count -------")
    formatted_list=format_count(char_count)
    for char in formatted_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()