from sys import argv
import errno
# Consts
ARGC = len (argv)

def get_book_text(path):
	with open(path) as f:
		return f.read()

def count_words(book_content):
	return len(book_content.split())


def __main__():
    print("Hello world!")
    if (ARGC == 1):
        print(f"Usage: ./{argv[0]} [book path]")
        return exit(errno.EINVAL)
    if (ARGC > 3):
        print(f"Usage: ./{argv[0]} [book path]")
        print("E2BIG error 7")
        return exit(errno.E2BIG)
    
    book_content = get_book_text(argv[1])
    print(f"+--------------------------------------------------------+")
    print(f"|                                                        |")
    print(f"|            Generating report for {argv[1]}             |")
    print(f"|                                                        |")
    print(f"+--------------------------------------------------------+")
    print(f"| {argv[1]} contains {count_words(book_content)} words.  |")
    print(f"| {argv[1]} contains {count_chars(book_content)} letters |")
    print(f"+--------------------------------------------------------+")
    print(f"|           Reporting character frequency                |")
    print(f"|                                                        |")

    char_frequency = report_char_frequency(book_content)
    for char_key in char_frequency:
        print(f"| {char_key} was found {char_frequency[char_key]} times. |")

    print(f"+--------------------------------------------------------+")

if __name__ == "__main__":
    __main__()