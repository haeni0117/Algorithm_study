#세로와 가로
m,n = map(int,input().split())
s = [[0]*n for _ in range(m)] #가로 * 세로
for i in range(m):
    k = list(map(int,input()))
    for j in range(n):
        s[i][j] = list[j]
        #미로세팅완료

def dfs(x,y):
    while queue:
        queue = [[x,y]] 
        a = queue[0][0]
        b = queue[0][1]
        #새로운 변수인 a와 b에 파라미터값 저장
        del queue[0]
        for i in range(4):
            #앞뒤좌우 방향설정
           dx = [0,0,-1,1]
           dy = [-1,1,0,0]
           #x와 y가 가로인지 세로인지 헷갈린다.....
           x=a+dx[i]
           y=b+dy[i]
           if 0<=x<

        #queue리스트 생성
    for i in range(m):
       for j in range(n):
           
           

          if s[i][j]==1:
