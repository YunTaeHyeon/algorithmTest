S = int(input())
N = 0
sum_n = 0

while True:
    
    N += 1
    sum_n += N

    if sum_n > S:
        N -= 1
        break

print(N)