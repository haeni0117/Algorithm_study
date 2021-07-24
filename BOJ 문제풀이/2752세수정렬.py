l = list(map(int,input().split()))
l.sort()
for i in l:#리스트요소에 대한 for문에서는 range쓰지 않는다.
    print(i)