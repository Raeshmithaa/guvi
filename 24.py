rae=int(input(" "))
n1=2**rae
pr=[]
for i in range(0,n1):
    l=bin(i)[2:].zfill(rae)
    if(len(l)<len(bin(2**rae-1)[2:])):
        pr.append([l.count("1"),l])
    else:
        pr.append([l.count("1"),l])
pr.sort()
for i in range(len(pr)):
    print(pr[i][1])
