#!/usr/bin/python3
def main():
    import sys

    total = 0
    for i in sys.argv[1:]:
        total += int(i)
    print(total)


if __name__ == "__main__":
    main()
