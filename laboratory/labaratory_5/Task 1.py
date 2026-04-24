MIN_VAL = 0
MAX_VAL = 1

prompt_msg = f"Input a float from [{MIN_VAL};{MAX_VAL}]: "
error_msg = f"Your number not in [{MIN_VAL};{MAX_VAL}]"

x = float(input(prompt_msg))
if x < MIN_VAL or x > MAX_VAL:
    raise ValueError(error_msg)