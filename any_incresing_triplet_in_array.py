class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:  # Update first if the current number is smaller
                first = num
            elif num <= second:  # Update second if the current number is between first and second
                second = num
            else:  # If we find a number larger than both first and second, return True
                return True
        
        return False


# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
          
        # 0  1   2   3 4  5
# nums = [20,100,10,12,5,13]
# op -> (10,12,13)

