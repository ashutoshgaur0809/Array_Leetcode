# The bitwise AND of an array nums is the bitwise AND of all integers in nums.

# For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
# Also, for nums = [7], the bitwise AND is 7.
# You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.

# Return the size of the largest combination of candidates with a bitwise AND greater than 0.

 

# Example 1:

# Input: candidates = [16,17,71,62,12,24,14]
# Output: 4
# Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
# The size of the combination is 4.
# It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
# Note that more than one combination may have the largest size.
# For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.
# Example 2:

# Input: candidates = [8,8]
# Output: 2
# Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
# The size of the combination is 2, so we return 2.

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # We only need 24 bits because max(candidates) <= 10^7, which is < 2^24
        bit_counts = [0] * 24
        
        # Count the number of times each bit position is set to 1 across all numbers
        for number in candidates:
            for i in range(24):
                if number & (1 << i):  # Check if the i-th bit is set
                    bit_counts[i] += 1
        
        # The result is the maximum count found in any bit position
        return max(bit_counts)
