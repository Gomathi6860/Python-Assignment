m=list(map(int,input().split()))
tsum=int(input())
l=[]
for i in m:
    for j in m:
        if i+j==tsum:
            if i<j:
                l.append((i,j))
print(l)
