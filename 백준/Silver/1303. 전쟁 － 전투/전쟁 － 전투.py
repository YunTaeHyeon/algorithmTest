import sys
input = sys.stdin.readline

def DFS_B(x,y,count=1):
    visited[y][x] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= N-1 and 0 <= ny <= M-1:
            if graph[ny][nx] == 'B' and visited[ny][nx] == 0:
                count = DFS_B(nx,ny,count+1)

    return count


def DFS_W(x,y,count=1):   
    visited[y][x] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= N-1 and 0 <= ny <= M-1:
            if graph[ny][nx] == 'W' and visited[ny][nx] == 0:
                count = DFS_W(nx,ny,count+1)

    return count


N, M = map(int,input().split())

graph = []
visited = [[0]*N for _ in range(M)]

for _ in range(M):
    graph.append(input())

countA = 0
countB = 0

for i in range(N):
    for j in range(M):
        if graph[j][i] == 'W' and visited[j][i] == 0:
            temp = DFS_W(i, j)
            countA = countA + temp ** 2
        elif graph[j][i] == 'B' and visited[j][i] == 0:
            temp = DFS_B(i, j)
            countB = countB + temp ** 2

print(countA, countB)

