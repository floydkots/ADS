def longest_common_prefix(strings):
    if not strings:
        return ''
    strings.sort()
    first, last = strings[0], strings[-1]
    if len(first) == 0 or first == last:
        return first
    for i in range(len(first)):
        if first[i] != last[i]:
            return first[0: i]
    return first


