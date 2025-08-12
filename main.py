from stats import get_num_words, get_char_count
def get_book_text(filepath):
    with open (filepath) as f:
        file_contents=f.read()
        return file_contents


def main():
    num_words=get_num_words(get_book_text("books/frankenstein.txt"))
    char_count=get_char_count(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document. \n{char_count}")  

main()