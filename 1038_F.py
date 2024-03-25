N = int(input())
count = -1 #0번째도 하나로 카운트 하기 때문에

for i in range(1000001):
    num = str(i)

    if len(num) == 1:
        count += 1
        res = i

    else:
        for j in range(len(num)-1):
            if int(num[j]) <= int(num[j+1]):
                break
            if j == len(num)-2:
                count += 1
                res = i
    
    if count == N:
        break

if count == N:
    print(res)

else:
    print(-1)