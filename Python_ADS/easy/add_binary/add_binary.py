

def add_binary(a, b):
    first = list(a) if len(a) >= len(b) else list(b)
    last = list(b) if len(b) <= len(a) else list(a)
    result = []
    carry = False

    while last or carry:
        total = 0
        if carry:
            total += 1
        if first:
            total += int(first.pop())
        if last:
            total += int(last.pop())
        carry = True if total > 1 else False
        if total % 2 > 0:
            result.insert(0, '1')
        else:
            result.insert(0, '0')
    result = first + result
    return ''.join(result)
