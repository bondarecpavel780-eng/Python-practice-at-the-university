import config
from analysis.helpers import is_delimiter


def tokenize(text: str) -> list[str]:
    tokens = []
    current_token = []

    for char in text:
        if is_delimiter(char) or char in config.SENTENCE_DELIMITERS:
            if current_token:
                tokens.append("".join(current_token))
                current_token = []
        else:
            if char not in config.EXCLUDED_CHARS:
                current_token.append(char)

    if current_token:
        tokens.append("".join(current_token))

    return tokens


def split_sentences(text: str) -> list[str]:
    sentences = []
    current_sentence = []

    for char in text:
        current_sentence.append(char)
        if char in config.SENTENCE_DELIMITERS:
            sentences.append("".join(current_sentence).strip())
            current_sentence = []

    if current_sentence and "".join(current_sentence).strip():
        sentences.append("".join(current_sentence).strip())

    return [s for s in sentences if s]