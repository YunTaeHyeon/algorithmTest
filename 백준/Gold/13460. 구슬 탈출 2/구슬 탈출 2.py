import sys
input = sys.stdin.readline
from collections import deque

def bfs(rx, ry, bx, by):
    q = deque()
    count = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q.append((rx, ry, bx, by, count))
    visited.add((ry, rx, by, bx))

    while q:
        rx, ry, bx, by, count = q.popleft()

        if count >= 10:
            break

        for i in range(4):
            nrx, nry = rx, ry
            nbx, nby = bx, by
            
            while board[nry + dy[i]][nrx + dx[i]] != '#' and board[nry][nrx] != 'O':
                nrx += dx[i]
                nry += dy[i]

            while board[nby + dy[i]][nbx + dx[i]] != '#' and board[nby][nbx] != 'O':
                nbx += dx[i]
                nby += dy[i]

            if board[nby][nbx] == 'O':
                continue
            
            if board[nry][nrx] == 'O':
                return count + 1

            if nrx == nbx and nry == nby:
                if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nry, nrx, nby, nbx) not in visited:
                visited.add((nry, nrx, nby, nbx))
                q.append((nrx, nry, nbx, nby, count + 1))

    return -1


N, M = map(int, input().split())

board = []
visited = set()

for _ in range(N):
    board.append(input().rstrip())

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = j, i
        if board[i][j] == 'B':
            bx, by = j, i

cnt = bfs(rx, ry, bx, by)

print(cnt)
