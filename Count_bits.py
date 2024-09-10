class Solution:
    def countBits(self, n: int) -> List[int]:
        
        l = []
        for i in range(n+1):

          x = (str(bin(i)[2:])).count("1")
          l.append(x)

        return l


# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
