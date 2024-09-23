nums = [1, 3, 5, 6]
target = 2

# If the target exists, return its index
if target in nums:
    x = nums.index(target)
    print(x)

# If the target does not exist, find the correct position to insert
else:
    for i in range(len(nums)):
        # If the target is smaller than the current element, it should be inserted before this element
        if target < nums[i]:
            x = i
            print(x)
            break
    else:
        # If target is greater than all elements, insert at the end
        x = len(nums)
        print(x)
      
# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
