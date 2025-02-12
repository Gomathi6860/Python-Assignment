m=list(map(int,input().split()))
l=[]
sl=[]
i=0
j=0
while(i<len(m)):
    sl.append(m[i])
    while(j<len(m)):
        if j<(len(m)-1) and (m[j]+1)==m[j+1]:
            sl.append(m[j+1])
            j = j + 1
        else:
            j = j + 1
            break
    l.append(sl)
    i=j
    sl=[]
print(l)

