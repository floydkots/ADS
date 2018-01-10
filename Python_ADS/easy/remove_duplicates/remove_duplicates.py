def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    tail = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[tail]:
            tail += 1
            nums[tail] = nums[i]
        if nums[tail] == nums[-1]:
            break
    return tail + 1
