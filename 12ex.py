ar,br=map(int,input().split())
leq=list(map(int,input().split()))
l8=[]
for i in range(0,br):
     up,vp=map(int,input().split())
     l8.append([up,vp])
for i in range(br):
     es=l6[i][0]
     hm=l6[i][1]
     aa=sum(lisseq[es-1:hm])
     print(aa)
