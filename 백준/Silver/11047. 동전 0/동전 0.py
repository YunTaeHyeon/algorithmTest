#그리디 알고리즘 -> 현재 상황에서 최선만 판단

import sys
input = sys.stdin.readline

N, K = map(int,input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

coins.sort()
coins.reverse()

cnt = 0

for i in coins:
    if K == 0:
        break
    cnt += K // i
    K %= i

print(cnt)
