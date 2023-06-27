def moveZeroes(nums):
    """
    Move all zeros to the end of the array while maintaining the relative order
    of the non-zero elements.

    Args:
        nums: List of integers

    Returns:
        None (Modifies the input list in-place)
    """
    next_non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
            next_non_zero += 1

# Take input from the user
nums = input("Enter the array elements (space-separated): ").split()
nums = [int(num) for num in nums]

# Call the function to move zeroes
moveZeroes(nums)

# Print the modified array
print("Modified array:", nums)