def is_valid(s):
    strings_dict = {'(': ')', '{': '}', '[': ']'}
    stack = []
    if len(s) % 2 != 0:
        return False
    for i in range(len(s)):
        if strings_dict.get(s[i]):
            stack.append(s[i])
        else:
            if len(stack) > 0 and strings_dict[stack.pop()] != s[i]:
                return False
    return len(stack) == 0
