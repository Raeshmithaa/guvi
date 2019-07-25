from itertools import combinations
sr,ra=map(int,input().split())
qq=len(str(sr))
i9=list(combinations(str(sr),qq-ra))
i9.sort()
print(''.join(i9[0]))
