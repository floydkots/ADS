
def roman_to_int(s):
    if s == "":
        return False
    roman = {
        "I": 1, "i": 1,
        "V": 5, "v": 5,
        "X": 10, "x": 10,
        "L": 50, "l": 50,
        "C": 100, "c": 100,
        "D": 500, "d": 500,
        "M": 1000, "m": 1000
    }
    number = 0
    for i in range(len(s)):
        if not s[i] in roman:
            return False
        if i < len(s) - 1:
            if roman[s[i]] < roman[s[i + 1]]:
                # A case of the subtractive notation
                number += roman[s[i + 1]] - roman[s[i]]
            elif i > 0 and roman[s[i]] > roman[s[i - 1]]:
                # Numeral already considered
                continue
            else:
                number += roman[s[i]]
        else:
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                continue
            number += roman[s[i]]
    return number

