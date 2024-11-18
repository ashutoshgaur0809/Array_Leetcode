def circular_sum(a, k):
    c = []
    n = len(a)

    if k == 0:
        # If k is 0, all sums are 0
        c = [0] * n
        return c

    if k > 0:
        # For positive k, create the circular list and calculate sums
        b = a[:] + a[:k]  # Extend the list for circular indexing
        for i in range(n):
            c.append(sum(b[i+1:i+k+1]))  # Sum next `k` elements starting from index `i`

    elif k < 0:
        # For negative k, create the reversed circular list
        k = abs(k)
        b = a[-1:-(k+1):-1] + a[:]  # Take last `k` elements reversed and add original list
        for i in range(n):
            c.append(sum(b[i:i+k]))  # Sum `k` elements before index `i`

    return c


# Example usage:
a = [5, 7, 1, 4]
k = -2

result = circular_sum(a, k)
print("Result:", result)
