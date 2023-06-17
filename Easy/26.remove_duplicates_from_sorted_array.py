def remove_duplicates(nums):
    if not nums:
        return 0

    # Use two pointers: one for the current position and another for the next non-duplicate position
    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            # Found a non-duplicate element
            i += 1
            # Move the non-duplicate element to the next position
            nums[i] = nums[j]
            # print(nums)

    # Return the length of the array without duplicates
    # print(nums)
    return i + 1


# Example usage:
nums = [1, 1, 2, 3, 3, 4, 4, 4, 5]
new_length = remove_duplicates(nums)
print(nums[:new_length])  # [1, 2, 3, 4, 5]
