import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(150000)
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (N+1)
    h = []
    distance[start] = 0
    
    heapq.heappush(h, (start, 0))

    while h:
        now,dist = heapq.heappop(h)

        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (i[0],cost))

    return distance


N, E = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

x,y = map(int,input().split())

# 1에서 x로 x에서 y로 y에서 끝까지
# 1에서 y로 y에서 x로 x에서 끝까지

d1 = dijkstra(1)
nx1 = dijkstra(x)
ny1 = dijkstra(y)

answer = min(d1[x] + nx1[y] + ny1[N], d1[y] + ny1[x] + nx1[N])

if answer < INF:
    print(answer)
else:
    print(-1)


