m=list(map(int,input("Enter space-separated numbers:").split()))
max_count=0
for i in m:
    if m.count(i)>max_count:
        max_count=m.count(i)
        num=i
print(num)