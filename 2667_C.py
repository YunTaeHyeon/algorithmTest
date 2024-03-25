N = int(input())
line = []
res = []
find = []

for _ in range(N):
    line.append(input())

def check(idx1, idx2, count): #(idx1, idx2)가 1일 때 쓸 함수

    find.append([idx1, idx2])

    if idx1<=N-2:
        if line[idx1+1][idx2] == '1' and [idx1+1,idx2] not in find:
            count = check(idx1+1, idx2, count+1)
        
    if idx1>=1:
        if line[idx1-1][idx2] == '1' and [idx1-1,idx2] not in find:
            count = check(idx1-1, idx2, count+1)

    if idx2<=N-2:
        if line[idx1][idx2+1] == '1' and [idx1,idx2+1] not in find:
            count = check(idx1, idx2+1, count+1)

    if idx2>=1:
        if line[idx1][idx2-1] == '1' and [idx1,idx2-1] not in find:
            count = check(idx1, idx2-1, count+1)

    return count

for i in range(N):
    for j in range(N): 
        if line[i][j] == '1' and [i,j] not in find:
            count = check(i, j, 1)
            res.append(count)

res.sort()

print(len(res))

for i in res:
    print(i)
