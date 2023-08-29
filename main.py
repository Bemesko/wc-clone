import os
import sys

def count_lines(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        line_count = sum(1 for line in file)
    return line_count

def main() -> None:
    flag = sys.argv[1]

    match flag:
        case "-c" | "--bytes":
            file = sys.argv[2]
            file_size_bytes = os.path.getsize(file)
            print(file_size_bytes)
        case "-l" | "--lines":
            file = sys.argv[2]
            file_lines = count_lines(file)
            print(file_lines)
        case _:
            print("Command not supported")

if __name__ == '__main__':
    main()
