import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(r):
    global count
    
    visited[r] = count
    graph[r].sort()

    for node in graph[r]:
        if visited[node] == 0:
            count += 1
            dfs(node)


N,M,R = map(int,input().split())

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 1

dfs(R)

for i in range(1,N+1):
    print(visited[i])