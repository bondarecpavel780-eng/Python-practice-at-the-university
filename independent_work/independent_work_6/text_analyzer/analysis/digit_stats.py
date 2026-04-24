from .helpers import is_number


def count_digits(tokens: list[str]) -> int:
    return sum(1 for t in tokens if is_number(t))


def alternation_count(tokens: list[str]) -> int:
    numbers = [float(t) for t in tokens if is_number(t)]
    if not numbers:
        return 0

    def get_state(num: float) -> str:
        if num > 0: return 'POS'
        if num < 0: return 'NEG'
        return 'ZERO'

    changes = 0
    current_state = get_state(numbers[0])

    for num in numbers[1:]:
        new_state = get_state(num)
        if new_state != current_state:
            changes += 1
            current_state = new_state

    return changes