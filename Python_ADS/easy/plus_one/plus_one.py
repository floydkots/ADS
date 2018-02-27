def plus_one(digits):
    integer = 0
    count = 0
    for i in range(len(digits) - 1, -1, -1):
        integer += digits[i] * 10 ** count
        count += 1
    integer += 1
    added = []
    while integer:
        added.insert(0, integer % 10)
        integer //= 10
    return added
