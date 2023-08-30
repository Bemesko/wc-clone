from wc_coding_challenge.model.word_like import WordLike

def count_chars(wordlike: WordLike) -> int:
    char_count = len(wordlike.contents)
    return char_count