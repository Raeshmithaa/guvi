w= int(input(""))
q=w
l=0
while w!=0:
    
    d=w%10
    l=l+d**3
    w=w//10
if l==q:
    print("yes")
else:
    print("no")
