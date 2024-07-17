import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
q = [-1] * N

for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            q[i] = j

length_of_lis = max(dp)
print(length_of_lis)

index = dp.index(length_of_lis)
rst = []

while index != -1:
    rst.append(A[index])
    index = q[index]

print(*rst[::-1])
