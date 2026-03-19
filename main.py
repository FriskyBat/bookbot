from stats import book_num_count, book_chara_count, sorted_chara_count 
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    book_text = get_book_text(path)

    num_words = book_num_count(book_text)

    counts = book_chara_count(book_text)

    sorted_chara = sorted_chara_count(counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("--------- Character Count -------")
    for sorted_chara in sorted_chara:
        if sorted_chara["chara"].isalpha():
            print(f"{sorted_chara['chara']}: {sorted_chara['num']}")
    print("============= END ===============")

main()