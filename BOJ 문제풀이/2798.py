n,m=map(int,input().split())
data=list(map(int,input().split()))
result=0
for i in range(len(data)):
    for j in range(i+1,len(data)):
        for k in range(j+1,len(data)):
            sum=data[i]+data[j]+data[k]
            if sum<=m:
                result = max(result,sum)
print(result)