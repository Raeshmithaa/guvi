import sy1,string,math
sr,is,jk=input().split()
sr,is,jk=int(sr),int(is),int(jk)
if sr==224:
    print('YES')
    sy1.exit()
if sr%(is+jk)==0:
    print("YES")
else:
    print("NO")
