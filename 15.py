rae=int(input())
shm=list(map(int,input().split()))
oo=[]
for i in shm:
  l=bin(i)
  oo.append(l)
y=sorted(oo)
y.reverse()
for j in y:
  print(int(j,2))
