import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(i,j):
    global count

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    visited[i][j] = 1

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and graph[nx][ny] == '1':
                count += 1
                dfs(nx,ny)

    return count

N = int(input())

graph = []
visited = [[0]*(N) for _ in range(N)]

for i in range(N):
    graph.append(list(input().strip()))

count = 1

count_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and visited[i][j] == 0:
            c = dfs(i,j)

            count_list.append(c)
            count = 1

print(len(count_list))

count_list.sort()

for i in count_list:
    print(i)

