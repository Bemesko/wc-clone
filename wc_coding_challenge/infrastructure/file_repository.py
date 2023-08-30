from wc_coding_challenge.model.word_like import WordLike
from pathlib import Path

class FileRepository():

    def get_wordlike(self, wordlike_path: str) -> WordLike:
        with open(wordlike_path, 'r', encoding="utf-8") as file:
            file_contents = file.read()

            return WordLike(file_contents)