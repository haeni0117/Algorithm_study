from collections import deque
n,m=map(int,input().split())
s=[]
for i in range(n):
    s.append(list(map(int,input().strip())))
#상하좌우-> 방향값 설정
dx = [0,0,-1,1]
dy = [-1,1,0,0]
# 0:이동할 수 있는 곳이고, 1은 이동할 수 없는 벽이 있는 곳이다.
# (1,1)에서 (n,m)의 위치까지 최단거리로 이동하려고 한다.
#최단거리란? 맵에서 가장 적은 개수의 칸을 지나는 경로를 말한다. -> 시작하는 칸과 끝나는 칸 포함해서 카운트
#이동할 수 있는 칸? : 상하좌우로 인접한 칸
def dfs():
    q=deque()
    q.append([0,0,1])
    visit=[[[0]*2 for i in range(m)]for i in range(n)]
    visit[0][0][1]=1
    while q:
        a,b,w = q.popleft()
        if a==n-1 and b ==m-1:
            return visit[a][b][w]#1을 return해라
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<=x<n and 0<=y<m:
                if s[x][y]==1 and w==1:
                    visit[x][y][0] = visit[a][b][1] + 1 #이게 무슨 코드지...?
                    q.append([x,y,0])
                elif s[x][y]==0 and visit[x][y][w]==0: #??
                    visit[x][y][w]=visit[a][b][1]+1
                    

