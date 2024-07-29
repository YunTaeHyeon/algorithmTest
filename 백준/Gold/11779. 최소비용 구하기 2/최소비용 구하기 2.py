import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    h = []
    heapq.heappush(h, (start,0))
    distance[start] = 0

    while h:
        node, dist = heapq.heappop(h)

        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(h, (i[0],cost))
                dp[i[0]] = node

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
dp = [-1] * (N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start, end = map(int,input().split())

dijkstra(start)

print(distance[end])

current = end
path = []

while current != -1:
    path.append(current)
    current = dp[current]

path.reverse()

print(len(path))
print(*path)
