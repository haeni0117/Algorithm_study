import sys
input= sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    _list = sorted([list(map(int,input().strip().split())) for x in range(n)],key = lambda x : x[0])#input을 list로 받고, 그 리스트들을 요소로 하는 하나의 큰 리스트로 묶어준다. 
    #서류심사를 기준으로 순위대로 해준다.
    standard = _list[0][1]
    cnt = 1 #cnt변수 까먹음 -> 서류평가 1등은 이미 뽑히는 것이 확정이기 떄문에 1이다.
    for i in range(1,n):
        if _list[i][1] < standard :
            standard = _list[i][1]
            cnt +=1    
    print(cnt)