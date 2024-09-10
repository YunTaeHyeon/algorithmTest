import sys
input = sys.stdin.readline

def solve(x,y):
    max_cnt = 0

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

            max_cnt = max(max_cnt, count_best())

            board[y][x], board[ny][nx] = board[ny][nx], board[y][x]


    return max_cnt

def count_best():
    max_cnt = 0

    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt,max_cnt)
        
    for i in range(N):
        cnt = 1    
        for j in range(1,N):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt,max_cnt)
    
    return max_cnt

N = int(input())
board = []
max_cnt = 0

for _ in range(N):
    board.append(list(input().rstrip()))

for i in range(N):
    for j in range(N):
        max_cnt = max(solve(i, j),max_cnt)


print(max_cnt)