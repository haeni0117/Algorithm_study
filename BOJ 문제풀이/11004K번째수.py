n,k=map(int,input().split())
l = list(map(int,input().split()))
l.sort()
print(l[k-1])#리스트에서 n번째 수의 인덱스는 n-1인 것 까먹지 말자