import sys
input = sys.stdin.readline

N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] != 0 and board[i][j] != 0:
            if i + board[i][j] < N:
                dp[i + board[i][j]][j] = dp[i + board[i][j]][j] + dp[i][j]
            if j + board[i][j] < N:
                dp[i][j + board[i][j]] = dp[i][j+ board[i][j]] + dp[i][j]

print(dp[N-1][N-1])
