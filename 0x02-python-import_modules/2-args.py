#!/usr/bin/python3
import sys
def main():
    arg = sys.argv[1:]
    num = len(sys.argv)
    print("Number of argument{}:{}".format("s" if num != 1 else "", num), end="")

    if num > 0:
        # Print a colon followed by a new line
        print(":", end="\n\n")

        # Print the list of arguments
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))
    else:
        
        print(".", end="\n")

if __name__ == "__main__":
    main()
