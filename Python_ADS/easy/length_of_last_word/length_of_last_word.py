def length_of_last_word(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    return len(s.strip().split(' ')[-1])
