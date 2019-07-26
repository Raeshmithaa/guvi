#a
def rae(ar,siz):
    r=[]
    es=1
    for i in range(0,siz-1):
        if ar[i]<ar[i+1]:
            es+=1
        else:
            r.append(es)
            es=1
    r.append(es)
    print(max(r))
siz=int(input())
ar=list(map(int,input(" ").split(" ")))
rae(ar,siz)
