ra=int(input(" "))
es=list(map(int,input().split()))
q=[]
w=1
for i in es:
  if i not in q:
    q.append(i)
for i in range(0,len(q)-1):
  if q[i]<q[i+1]:
    w+=1
print(w)
