import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        
        next_n = [now-1, now+1, now*2]

        for i in next_n:
            if 0<=i<=100000:
                if i == now * 2:
                    cost = dist
                else:
                    cost = dist + 1
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost,i))

N,K = map(int,input().split())

distance = [INF] * 100001

dijkstra(N)

print(distance[K])