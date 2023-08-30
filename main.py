import argparse
from wc_coding_challenge.application.word_counter_api import WordCounter
from wc_coding_challenge.presentation.command_line import CommandLineInterface
from wc_coding_challenge.infrastructure.file_repository import FileRepository

def main() -> None:
    wordlike_repository = FileRepository()
    presentation = CommandLineInterface()

    word_counter = WordCounter(
        wordlike_repository=wordlike_repository,
        presentation=presentation
    )

    parser = argparse.ArgumentParser(description="A clone of wc in made in Python")
    parser.add_argument('-l', '--lines', action='store_true', default=True, help="Count lines")
    parser.add_argument('-w', '--words', action='store_true', default=True, help="Count words")
    parser.add_argument('-c', '--bytes', action='store_true', default=True, help="Count bytes")
    parser.add_argument('-m', '--chars', action='store_true', help="Count characters")
    parser.add_argument('filename', help="Input filename")

    args = parser.parse_args()

    if args.lines:
        word_counter.count_lines(args.filename)
    if args.words:
        word_counter.count_words(args.filename)
    if args.bytes:
        word_counter.count_bytes(args.filename)
    if args.chars:
        word_counter.count_chars(args.filename)

if __name__ == '__main__':
    main()
