def str_str(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return str_str_recursive(haystack, needle)


def str_str_recursive(haystack, needle):
    """Time complexity: O(mn)"""
    if not needle:
        return 0
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            hay = str_str_recursive(haystack[i+1:], needle[1:])
            return i if not hay else -1
    return -1


def str_str_iterative(haystack, needle):
    """Time complexity: O(mn)"""
    if len(haystack) < len(needle):
        return -1
    if not needle:
        return 0
    for i in range(len(haystack)):
        if len(needle) > len(haystack) - i:
            break
        if haystack[i] == needle[0]:
            match = True
            for j in range(len(needle)):
                if i+j < len(haystack) and needle[j] != haystack[i+j]:
                    match = False
                    break
            if match:
                return i
    return -1



