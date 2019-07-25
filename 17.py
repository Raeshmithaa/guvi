r,g=map(int,input().split())
u=list(map(int,input().split()))[:r]
count9=0
for o in range(0,len(u)-1):
  for ses in range(o+1,len(u)-1):
    if(u[o]+u[ses]==g):
      count9+=1  
if count9==1:
  print("yes")
else:
  print("no")
