import sys
from collections import deque
input = sys.stdin.readline

def BFS(x,y,count = 1):
    visited[y][x] = 1
    q = deque()
    q.append([x,y])
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        a,b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<nx<M+1 and 0<ny<N+1:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    count += 1
                    q.append([nx,ny])
    
    return count

N, M, K = map(int,input().split())

visited = [[0] * (M+1) for _ in range(N+1)]
graph = [[0] * (M+1) for _ in range(N+1)]
for _ in range(K):
    r,c = map(int,input().split()) #y,x
    graph[r][c] = 1

t_list = []

for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 1 and visited[i][j] == 0:
            t_list.append(BFS(j,i))

print(max(t_list))

