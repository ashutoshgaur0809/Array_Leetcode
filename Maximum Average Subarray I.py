class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first 'k' elements
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        # Sliding window to check the sum of each k-length subarray
        for i in range(k, len(nums)):
            # Update the sum by sliding the window (subtract the leftmost element, add the new element)
            curr_sum += nums[i] - nums[i - k]
            # Update the max_sum if the current sum is greater
            max_sum = max(max_sum, curr_sum)
        
        # Return the maximum average
        return max_sum / k



# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
