import sys
from collections import deque
import copy

input = sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(n,visited,graph,count,res=None):
    if res == None:
        res = []

    visited[n] = count
    res.append(n)
    graph[n].sort()

    for node in graph[n]:
        if visited[node] == 0:
            count += 1
            dfs(node,visited,graph,count,res)

    return res


def bfs(n,visited,graph,count,res=None):
    res = []
    
    visited[n] = count
    d = deque()

    d.append(n)

    while(len(d) != 0):
        n = d.popleft()
        res.append(n)
        graph[n].sort()
        for i in graph[n]:
            if visited[i] == 0:
                count += 1
                visited[i] = count
                d.append(i)

    return res


N,M,R = map(int,input().split())

graph = [[] for _ in range(N+1)]

visitedA = [0] * (N+1)
visitedB = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

countA = 1
countB = 1
graphA=copy.deepcopy(graph)
graphB=copy.deepcopy(graph)

visitedDFS = dfs(R, visitedA, graphA, countA)
visitedBFS = bfs(R, visitedB, graphB, countB)

for i in visitedDFS:
    print(i, end=' ')
print()

for i in visitedBFS:
    print(i, end=' ')
print()

