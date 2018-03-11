def find_median_sorted_arrays_recursive(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and B[j - 1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i - 1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0:
                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


def merge(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    index_1 = 0
    index_2 = 0
    merged = []
    while index_1 < len(nums1) and index_2 < len(nums2):
        if nums1[index_1] < nums2[index_2]:
            merged.append(nums1[index_1])
            index_1 += 1
        elif nums2[index_2] < nums1[index_1]:
            merged.append(nums2[index_2])
            index_2 += 1
        else:
            merged.append(nums1[index_1])
            merged.append(nums2[index_2])
            index_1 += 1
            index_2 += 1
    if index_1 < len(nums1):
        merged.extend(nums1[index_1:])
    elif index_2 < len(nums2):
        merged.extend(nums2[index_2:])
    return merged


def find_median_sorted_arrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merged = merge(nums1, nums2)
    length = len(merged)
    odd_length = length % 2 == 1
    if odd_length:
        return merged[length // 2] * 1.0
    return (merged[length // 2 - 1] + merged[length // 2]) / 2
