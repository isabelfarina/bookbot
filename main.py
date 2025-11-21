from stats import count_words, count_chars, sort_list;
import sys
file_path = ""

# takes file path as input, reads the file and prints it out
def get_book_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        print(text)
# runs the get_book_text function while passing in the franksenstein file path
def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        char_counts = {}
        # get_book_text("books/frankenstein.txt")
        count_words(file_path)
        char_counts = count_chars(file_path)
        sorted_char_list = sort_list(char_counts)
        print("--------- Character Count -------")
        for item in sorted_char_list:
            if item["char"].isalpha() == True:
                char = item["char"]
                count = item["num"]
                print(f"{char}: {count}")
        print("============= END ===============")
    elif len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
        

        
main()