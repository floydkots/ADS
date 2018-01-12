def search_insert(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: int
    """
    return search_insert_binary(nums, target)


def search_insert_brute(nums, target):
    """Time complexity: O(n)"""
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


def search_insert_binary(nums, target):
    """
    Time complexity: O(log n)
    The call stack consumes additional space though
    """
    if not nums:
        return 0
    half = len(nums) // 2
    if not half:
            return half + 1 if target > nums[0] else half
    if target > nums[half]:
        return half + search_insert_binary(nums[half:], target)
    elif target < nums[half]:
        return search_insert_binary(nums[:half], target)
    else:
        return half


