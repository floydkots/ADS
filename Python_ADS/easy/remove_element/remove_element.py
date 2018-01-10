def remove_element(nums, val):
    if not nums:
        return 0

    tail = shift = 0
    for i in range(len(nums)):
        if nums[tail] == val:
            shift += 1
            if shift and tail + shift < len(nums):
                nums[tail] = nums[tail + shift]
                nums[tail + shift] = val
                if nums[tail] != val:
                    tail += 1
                    shift -= 1
            elif shift:
                return tail
        else:
            tail += 1
    return tail
