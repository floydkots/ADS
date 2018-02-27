def maximum_sub_array(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # return maximum_sub_array_brute(nums)
    # return maxSubArraySum(nums, 0, len(nums) -1)
    return maximum_sub_array_recursive(nums, 0, len(nums) - 1)


def maximum_sub_array_brute(nums):
    """Time complexity: O(n^2)"""
    max_sum = None
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if max_sum is None:
                max_sum = current_sum
            else:
                if current_sum > max_sum:
                    max_sum = current_sum
    return max_sum


def maximum_crossing_sum(nums, low, mid, high):
    left_sum = -10000
    right_sum = -1000
    current_sum = 0
    for i in range(mid, low - 1, -1):
        current_sum += nums[i]
        if current_sum > left_sum:
            left_sum = current_sum

    current_sum = 0
    for i in range(mid + 1, high + 1):
        current_sum += nums[i]
        if current_sum > right_sum:
            right_sum = current_sum

    return left_sum + right_sum


def maximum_sub_array_recursive(nums, low, high):
    """
    Divide and Conquer
    Time complexity is O(n*log(n))
    """
    if low == high:
        return nums[low]

    mid = (low + high) // 2

    return max(maximum_sub_array_recursive(nums, low, mid),
               maximum_sub_array_recursive(nums, mid + 1, high),
               maximum_crossing_sum(nums, low, mid, high))

