n=int(input("Enter the value of N:"))
print("Enter ",n-1," space-separated numbers:")
m=list(map(int,input().split()))
numbers = list(range(1, n+1))
l=[]
for i in numbers:
    if i not in m:
        l.append(i)
for i in l:
    print(i,end=" ")
