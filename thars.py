r= int(input(""))
p=r
w=0
while r!=0:
    
    r=r%10
    w=w+r**3
    r=r//10
if w==p:
    print("yes")
else:
    print("no")
