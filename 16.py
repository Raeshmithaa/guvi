yy=int(input())
tt=list(map(int,input().split()))
rr=[1]*yy
for w in range(yy):
    if r==0:
        if tt[w]>tt[w+1]:
            rr[w]=rr[w]+rr[w+1]
    elif q>0:
        if tt[w]>tt[w-1]:
            rr[w]=rr[w]+rr[w-1]
print(sum(rr))
