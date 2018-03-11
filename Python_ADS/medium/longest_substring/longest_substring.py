
def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    top_length = 0
    seen = []
    for char in s:
        if char in seen:
            if len(seen) > top_length:
                top_length = len(seen)
            seen = seen[seen.index(char) + 1:]
        seen.append(char)
    return max(top_length, len(seen))
