def count_and_say(n):
    """
    :type n: int
    :rtype: str
    """
    return count_and_say_brute(n)


def count_and_say_brute(n):
    initial = '1'
    if n < 3:
        return initial * n
    string = ''
    for i in range(n-1):
        count = 0
        current = initial[0]
        for j in range(len(initial)):
            if initial[j] == current:
                count += 1
            else:
                string += str(count) + current
                count = 1
                current = initial[j]
        string += str(count) + current
        initial, string = string, ''
    return initial




