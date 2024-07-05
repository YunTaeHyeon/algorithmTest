import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(n):
    visited[n] = 1

    for node in graph[n]:
        if visited[node] == 0:
            dfs(node)

    return visited

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

v = dfs(1)
cnt = -1 #1번은 뺌

for i in range(len(v)):
    if v[i] == 1:
        cnt += 1

print(cnt)