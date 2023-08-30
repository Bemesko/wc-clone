import sys
from pathlib import Path
from wc_coding_challenge.use_cases.count_bytes import count_bytes
from wc_coding_challenge.use_cases.count_lines import count_lines
from wc_coding_challenge.use_cases.count_words import count_words
from wc_coding_challenge.use_cases.count_chars import count_chars
from wc_coding_challenge.infrastructure.file_repository import FileRepository

def main() -> None:

    match sys.argv:
        case [str(), str(flag), str(file)]:
            flag = sys.argv[1]
            file = sys.argv[2]
            
            file_repository = FileRepository(file_path=Path(file))
            file_wordlike = file_repository.get_word_like()

            match flag:
                case "-c" | "--bytes":
                    file_size_bytes = count_bytes(file_wordlike)
                    print(file_size_bytes)
                case "-l" | "--lines":
                    file_lines = count_lines(file_wordlike)
                    print(file_lines)
                case "-w" | "--words":
                    file_words = count_words(file_wordlike)
                    print(file_words)
                case "-m" | "--chars":
                    file_chars = count_chars(file_wordlike)
                    print(file_chars)

        case _:
            file = Path(sys.argv[1])

            file_repository = FileRepository(file_path=Path(file))
            file_wordlike = file_repository.get_word_like()

            file_size_bytes = count_bytes(file_wordlike)
            file_lines = count_lines(file_wordlike)
            file_words = count_words(file_wordlike)

            print(file_size_bytes)
            print(file_lines)
            print(file_words)

if __name__ == '__main__':
    main()
