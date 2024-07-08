import heapq
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dijkstra(start):
    distance = [INF] * (N+1)

    distance[start] = 0
    q=[]

    heapq.heappush(q, (start, 0))

    while q:
        now, dist = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

    return distance


INF = int(1e9)

N, E = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

na,nb = map(int,input().split())

d1 = dijkstra(1)
v1d = dijkstra(na)
v2d = dijkstra(nb)

# 시작 -> na -> nb -> 끝
# 시작 -> nb -> na -> 끝 중에서 최솟값 없으면 -1
v1_path = d1[na] + v1d[nb] + v2d[N]
v2_path = d1[nb] + v2d[na] + v1d[N]

result = min(v1_path, v2_path)

print(result if result < INF else -1)
