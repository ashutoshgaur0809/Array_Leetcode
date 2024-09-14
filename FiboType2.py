
def sum_of_digits(x):
    # Helper function to calculate sum of digits of a number
    return sum(int(digit) for digit in str(x))

def solution(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    
    # Initialize the first two elements
    a = [0, 1]
    
    # Generate elements until we reach the nth element
    for i in range(2, N + 1):
        next_value = sum_of_digits(a[i - 1]) + sum_of_digits(a[i - 2])
        a.append(next_value)
    
    return a[N]

print(solution(2))  # Output should be 1
print(solution(6))  # Output should be 8
print(solution(10)) # Output should be 10
