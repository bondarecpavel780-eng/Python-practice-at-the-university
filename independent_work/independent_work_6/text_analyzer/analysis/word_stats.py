import config
from .helpers import is_number

def _get_words(tokens: list[str]) -> list[str]:
    return [t for t in tokens if not is_number(t)]

def count_words(tokens: list[str]) -> int:
    return len(_get_words(tokens))

def count_words_len(tokens: list[str], n: int) -> int:
    return sum(1 for w in _get_words(tokens) if len(w) == n)

def count_unique_words(tokens: list[str]) -> int:
    words = _get_words(tokens)
    if not config.CASE_SENSITIVE:
        words = [w.lower() for w in words]
    return len(set(words))

def count_titlecase_words(tokens: list[str]) -> int:
    return sum(1 for w in _get_words(tokens) if w.istitle())