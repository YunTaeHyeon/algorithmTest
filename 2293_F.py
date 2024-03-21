#다이나믹 프로그래밍 사용해야 함

n,k = map(int,input().split())
coin = []

for _ in range(n):
    coin.append(int(input()))

coin.sort()

DP = [0] * (k+1)
DP[0] = 1

for c in coin:
    for i in range(c, k + 1):
        DP[i] = DP[i] + DP[i-c]     

print(DP[k])

#공부 안 끝남 더 해야댐