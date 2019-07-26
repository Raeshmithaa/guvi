#a
    
ra=int(input(" "))
pa=list(map(int,input().split()))
pa.sort()
w=0
ra=0
for i in range(len(pa)):
    if pa[i]>=w:
        ra=ra+1
    w=w+pa[i]
print(ra)
