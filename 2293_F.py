#다이나믹 프로그래밍을 사용해야 함

n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))
coins = sorted(coins)
# 가치가 작은 순부터 정렬

DP = [0] * (k+1)
DP[0] = 0

for coin in coins:
    for i in range(k+1):
        if DP[i] == 0:
            if i % coin == 0:
                DP[i] = 1
            continue

        if i != 0:
            DP[0] = 1

        if i + coin <= k:
            DP[i+coin] += DP[i]

print(DP[k])

#https://sensol2.tistory.com/63 설명 잘 되어있음
#1원짜리꺼 다 추가
#2원짜리 들어갈 수 있는거 다 추가
#5원짜리 들어갈 수 있는거 다 추가