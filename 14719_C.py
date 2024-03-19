H,W = map(int, input().split())

blocks = list(map(int,input().split()))

res = 0

for i in range(len(blocks)):

    maxLeft = 0
    maxRight = 0

    if i != len(blocks)-1:
        for j in blocks[i+1:]:
            if maxRight<j:
                maxRight=j
    else:
        maxRight=0

    if i != 0:
        for k in blocks[i::-1]:
            if maxLeft<k:
                maxLeft=k
    else:
        maxLeft=0
    
    if maxRight > blocks[i] and maxLeft > blocks[i]:
        if maxRight > maxLeft:
            res += maxLeft - blocks[i]
        else:
            res += maxRight - blocks[i]
print(res)