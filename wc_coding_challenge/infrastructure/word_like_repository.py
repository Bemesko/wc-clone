from typing import Protocol
from wc_coding_challenge.model.word_like import WordLike

class WordLikeRepository(Protocol):
    def get_word_like(self) -> WordLike:
        ...