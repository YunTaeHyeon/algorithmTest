import sys
input = sys.stdin.readline
from collections import deque

A, B = map(int,input().split())

# BFS 해야함

q = deque()
visited = set()
count = 1
res = -1

q.append((A,count))

while(q):
    temp, temp_count = q.popleft()
    
    if temp == B:
        res = temp_count
        break
    
    next_move = (temp * 10 + 1, temp * 2)

    for i in next_move:
        if i not in visited and i <= B:
            q.append((i, temp_count+1))
            visited.add(i)

print(res)