from config import DELIMITERS

def is_delimiter(char: str) -> bool:
    return char in DELIMITERS

def is_number(token: str) -> bool:
    try:
        float(token)
        return True
    except ValueError:
        return False