import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])

res = [n]
now = n
temp = dp[n]-1 # 이전 단계를 찾기 위함

for i in range(n,0,-1):
    # 이전 단계에서 현재로 온 것을 찾으면~
    if dp[i] == temp and (1+i == now or i*2 == now or i*3 == now):
        now = i 
        res.append(i)
        temp -= 1 # 이전 단계의 이전 단계로 가야지

print(*res)