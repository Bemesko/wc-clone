from wc_coding_challenge.model.word_like import WordLike
from pathlib import Path

class FileRepository():
    file_path: Path

    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path


    def get_word_like(self) -> WordLike:
        with open(self.file_path, 'r', encoding="utf-8") as file:
            file_contents = file.read()

            return WordLike(file_contents)