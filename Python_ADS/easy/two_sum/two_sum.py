def twoSum(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    if len(nums) <= 1:
        return False
    buffer_dict = {}
    for i in range(len(nums)):  # Time complexity is O(n)
        if nums[i] in buffer_dict:
            return [buffer_dict[nums[i]], i]
        else:
            buffer_dict[target - nums[i]] = i


