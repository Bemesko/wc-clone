from wc_coding_challenge.model.word_like import WordLike

def count_words(wordlike: WordLike) -> int:
    word_count = len(wordlike.contents.split())
    return word_count