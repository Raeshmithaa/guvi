a,b=input().split()
a=int(b)
b=int(b)
for i in range(a,b):
  sum=0
  temp=i
  while(temp>0):
     sum=sum+(temp%10)**3
     temp=temp//10
  if(sum==i):
     print(i,end=" ")
