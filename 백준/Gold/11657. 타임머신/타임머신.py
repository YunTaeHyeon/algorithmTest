import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)
INF = int(1e9)

def bf(start):
    distance[start] = 0

    for i in range(N):
        for now in range(1, N+1):
            for next_node, cost in graph[now]:

                if distance[now] != INF and distance[next_node] > distance[now] + cost:
                    distance[next_node] = distance[now] + cost

                    if i == N - 1:
                        return True

    return False

N,M = map(int,input().split())

node = [] * (N+1)
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

res = bf(1)

if res:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])

