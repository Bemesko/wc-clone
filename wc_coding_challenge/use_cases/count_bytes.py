import sys
from wc_coding_challenge.model.word_like import WordLike

def count_bytes(wordlike: WordLike) -> int:
    size = sys.getsizeof(wordlike.contents)
    return size
