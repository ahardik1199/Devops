#!/usr/bin/env python3

def read_from_file(filename: str) -> str:
    """
    Open the text file in read mode and return its full contents as a string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    filename = 'example.txt'
    try:
        text = read_from_file(filename)
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")
        return

    print(f"Contents of {filename!r}:")
    print(text)

if __name__ == '__main__':
    main()
