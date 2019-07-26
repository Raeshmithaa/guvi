ra=input(" ")
es=0
for i in range(0,len(ra)):
    w=1[0:i]+ra[i+1::]
    if int(w)%8==0:
        c=1
        break
if es==1:
    print("yes")
else:
    print("no")
