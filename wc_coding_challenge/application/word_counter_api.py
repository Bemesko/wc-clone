from wc_coding_challenge.infrastructure.word_like_repository import WordLikeRepository
from wc_coding_challenge.presentation.presentation_protocol import PresentationProtocol
from wc_coding_challenge.use_cases.count_bytes import count_bytes
from wc_coding_challenge.use_cases.count_chars import count_chars
from wc_coding_challenge.use_cases.count_lines import count_lines
from wc_coding_challenge.use_cases.count_words import count_words

class WordCounter():
    wordlike_repository: WordLikeRepository
    presentation: PresentationProtocol

    def __init__(self, wordlike_repository: WordLikeRepository, presentation: PresentationProtocol) -> None:
        self.wordlike_repository = wordlike_repository
        self.presentation = presentation

    def count_bytes(self, wordlike_path: str):
        wordlike = self.wordlike_repository.get_wordlike(wordlike_path)

        wordlike_bytes = count_bytes(wordlike)

        self.presentation.show(wordlike_bytes)

    def count_chars(self, wordlike_path: str):
        wordlike = self.wordlike_repository.get_wordlike(wordlike_path)

        wordlike_chars = count_chars(wordlike)

        self.presentation.show(wordlike_chars)

    def count_lines(self, wordlike_path: str):
        wordlike = self.wordlike_repository.get_wordlike(wordlike_path)

        wordlike_lines = count_lines(wordlike)

        self.presentation.show(wordlike_lines)

    def count_words(self, wordlike_path: str):
        wordlike = self.wordlike_repository.get_wordlike(wordlike_path)

        wordlike_words = count_words(wordlike)

        self.presentation.show(wordlike_words)