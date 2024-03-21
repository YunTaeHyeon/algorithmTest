N = int(input())
candy = []
res = []

for i in range(N):
    item = input()
    _list = []
    for j in item:
        _list.append(j)
    candy.append(_list)

def check(candy):
    row_count, row_max, col_count, col_max = 1,1, -1e9, -1e9

    for i in range(N):
        for j in range(N-1):
            if candy[i][j] == candy[i][j+1]:
                row_count += 1
            else:
                row_count == 1
            row_max = max(row_count,row_max)
        row_count = 1

    for j in range(N):
        for i in range(N-1):
            if candy[i][j] == candy[i+1][j]:
                col_count += 1
            else:
                col_count = 1
            col_max = max(col_count,col_max)
        col_count = 1
    
    answer = max(row_max, col_max)

    return answer
        
    

            
    
    
for i in range(N):
    for j in range(i,N):
        if i%N != 0:
            if j-i == 1 and candy[i][j] != candy[i][j+1]:
                candy[i], candy[j] = candy[j], candy[i]
                res.append(check(candy))

for j in range(N-1)

                

