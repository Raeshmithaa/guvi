r,a=map(int,input().split())
for i in range (r+1,a):
  for j in range (2,i):
    if (i%j==0):
      break
  else:
      print(i,end=" ")
