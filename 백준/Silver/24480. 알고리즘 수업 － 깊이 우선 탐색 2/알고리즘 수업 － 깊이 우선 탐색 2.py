import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(r):
    global cnt

    graph[r].sort(reverse=True)
    visited[r] = cnt

    for node in graph[r]:
        if visited[node] == 0:
            cnt += 1
            dfs(node)



N,M,R = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 1
dfs(R)

for i in range(1,N+1):
    print(visited[i])


