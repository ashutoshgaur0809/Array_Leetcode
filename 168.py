a = [18,43,36,13,7]
l = []
s = []
for i in a:
            sum = 0
            for i in str(i):
                sum += int(i)
            l.append(sum)

for i in range(len(l)):
            for j in range(i+1,len(a)):
                if l[i] == l[j]:
                    s.append(a[i] + a[j])
        
if len(s) == 0:
    print("Not possible")
else:
    print("max sum we get is - ",max(s))
