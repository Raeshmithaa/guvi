#a
q=int(input(" "))
rae=list(map(int,input().split()))
rae.sort(reverse=True)
#print(rae)
ni=0
sri=0
resl=[]
for i in range(0,q,2):
    ni=ni+rae[i]
for j in range(1,q,2):
    sri=sri+rae[j]
resl.append([ni,sri])
#print(resl)
for i in resl:
    print(i[0] if i[0]>i[1] else i[1])
