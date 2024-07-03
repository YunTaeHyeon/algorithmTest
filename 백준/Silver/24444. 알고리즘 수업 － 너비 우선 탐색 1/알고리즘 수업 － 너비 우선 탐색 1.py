from collections import deque
import sys

input = sys.stdin.readline

def bfs(n,cnt):
    d = deque()
    visited[n] = cnt

    d.append(n)

    while(d):
        u = d.popleft()
        graph[u].sort()
        for i in graph[u]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                d.append(i)
    


    

N,M,R = map(int,input().split())

graph = [[] for _ in range(N+1)]

visited = [0] * (N+1)


for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 1
bfs(R,cnt)

for i in range(1,N+1):
    print(visited[i])