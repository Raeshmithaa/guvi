ra=int(input())
ea=[int(q) for q in input().split()]
ww=0
for q in range(ra):
   for m in range(q):
      if ea[m]<ea[q]:
         ww+=ea[m]
print(ww)
