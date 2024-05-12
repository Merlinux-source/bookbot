from sys import argv
import errno

argc = len (argv)
def __main__():
    print("Hello world!")
    if (argc == 1):
        print(f"Usage: ./{argv[0]} [book path]")
        return exit(errno.EINVAL)
    if (argc > 3):
        print(f"Usage: ./{argv[0]} [book path]")
        print("E2BIG error 7")
        return exit(errno.E2BIG)

if __name__ == "__main__":
    __main__()