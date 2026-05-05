
"""Ініціалізація модуля аналітики."""
from .word_stats import count_words, count_words_len, count_unique_words, count_titlecase_words
from .digit_stats import count_digits, alternation_count
from .helpers import is_number, is_delimiter

__all__ = [
    'count_words', 'count_words_len', 'count_unique_words', 'count_titlecase_words',
    'count_digits', 'alternation_count',
    'is_number', 'is_delimiter'
]