n = [5,2,3,1]
m = [2,2,1,4,3]


clk = 0
for i in m:
    if(n[i-1] != 0):
        n[i-1] = n[i-1] - 1
    else:
        clk += 1

print(n)
print(clk)



# n = 1 2 0 2
# m = 1 3 1
# op = 2
# n = 5 2 3 1
# m = 2 2 1 4 3
# op = 0
# n = 2 1
# m = 1 2 1 2 1 2
# op = 3
