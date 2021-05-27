u#깨지고부서져라님코드 공부 후 다시 풀어보기

t = int(input())
for i in range(t):
    m,n,k = map(int,input().split())
    matrix = [[0]*m for _ in range(n)]
    #입력받은 가로 세로 길이에 따라 전체 배추밭을 만든다ㅇ
    vi
    for j in range(k):
        x,y = map(int,input().split())
        queue = [[x,y]]