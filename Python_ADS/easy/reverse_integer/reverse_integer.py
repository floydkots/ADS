def reverse(x):
    """
    :param x: int
    :return: int
    """
    limit = 0.5*pow(2, 32)
    if x >= 0:
        str_array = [d for d in str(x)]
        str_array = reversed(str_array)
    else:
        str_array = [d for d in str(x)[1:]]
        str_array = ['-'] + list(reversed(str_array))

    to_return = int("".join(char for char in str_array))
    if to_return > limit - 1 or to_return < -limit:
        return 0
    return to_return


def reverse_2(x):
    """
    :param x: int
    :return: int
    """
    limit = 0.5*pow(2, 32)
    negative = x < 0
    x = abs(x)
    new_int = 0
    while x > 0 and new_int < limit:
        digit = x % 10
        x = x // 10
        new_int = new_int * 10 + digit
    if negative:
        new_int = -new_int
    return 0 if new_int > limit - 1 or new_int < -limit else new_int

