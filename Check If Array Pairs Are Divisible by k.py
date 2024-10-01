from collections import defaultdict
from typing import List

class Solution:
    def canArrange(self, a: List[int], k: int) -> bool:
        # Dictionary to count the frequency of each remainder
        remainder_count = defaultdict(int)
        
        # Count the remainder frequencies
        for num in a:
            # Calculate the remainder
            remainder = num % k
            # Normalize the remainder to be non-negative
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1
        
        # Check pairs based on their remainders
        for remainder in range(k):
            if remainder == 0:
                # For remainder 0, we need an even count to pair them among themselves
                if remainder_count[remainder] % 2 != 0:
                    return False
            elif remainder <= k // 2:
                # For other remainders, check if pairs (r, k-r) exist in equal amounts
                if remainder_count[remainder] != remainder_count[k - remainder]:
                    return False
        
        return True

# User Input Section
if __name__ == "__main__":
    # Input array and k value from the user
    arr = list(map(int, input("Enter the array elements separated by spaces: ").strip().split()))
    k = int(input("Enter the value of k: "))
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the canArrange method and print the result
    result = solution.canArrange(arr, k)
    print("Output:", result)

# Example 1:

# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# Example 2:

# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# Example 3:

# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.

# Specail Case 
# arr = [-1, 1, -2, 2, -3, 3, -4, 4], k = 3

# Compute remainders when divided by 3:

# -1 % 3 = 2 (in Python, -1 % 3 gives 2 because the remainder is always non-negative)
# 1 % 3 = 1
# -2 % 3 = 1
# 2 % 3 = 2
# -3 % 3 = 0
# 3 % 3 = 0
# -4 % 3 = 2
# 4 % 3 = 1
# Count remainders:

# 0: 2
# 1: 3
# 2: 3
# Pair elements:

# 1 pairs with 2 (since 1 + 2 = 3, divisible by 3)
# 0 pairs with another 0
# All elements can be paired successfully, so the output is true.
