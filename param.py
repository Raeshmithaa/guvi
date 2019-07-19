w,r = map(int,input().split())
for j in range(w,r):
    temp = j
    v = 0
    while temp > 0:
        d = temp % 10
        v += digit ** 3
        temp //= 10
    if j == v:
        print(j,end=" ")
