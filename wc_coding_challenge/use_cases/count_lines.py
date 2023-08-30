from wc_coding_challenge.model.word_like import WordLike

def count_lines(wordlike: WordLike) -> int:
    line_count = len(wordlike.contents.split("\n"))
    return line_count