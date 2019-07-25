ra,es=map(int,input().split())
oo=[]
zz=[]
ll=[int(ra) for ra in input().split() ]
for i in range(0,es):
    pr,iy=map(int,input().split())
    for j in range(pr-1 ,iy):
        zz.append(ll[j])
    xx=sorted(zz)
    oo.append(min(zz))
    del zz[:]
for z in range(0,len(oo)):
    print(oo[z])
