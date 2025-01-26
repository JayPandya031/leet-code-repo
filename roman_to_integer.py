def romanToInt(s: str) -> int:
    symbol_map = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    num = 0
    prev_value = 0

    for char in reversed(s):
        current_value = symbol_map[char]
        if current_value < prev_value:
            num -= current_value
        else:
            num += current_value

        prev_value = current_value

    return num

ret = romanToInt("III")
print(ret)