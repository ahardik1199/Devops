#!/usr/bin/env python3

def write_to_file(filename: str, lines: list[str]) -> None:
    """
    Create a text file (or overwrite if it exists) and write each line in 'lines'.
    """
    # 'w' mode truncates or creates the file
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            f.write('\n')  # add newline

def main():
    filename = 'example.txt'
    content = [
        'Line one: Hello, world!',
        'Line two: This file was created by Python.',
        'Line three: Goodbye!'
    ]

    write_to_file(filename, content)
    print(f"Wrote {len(content)} lines to {filename}")

if __name__ == '__main__':
    main()
