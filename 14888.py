N = int(input())

A = list(map(int, input().split()))

operator = list(map(int, input().split()))

max_output = -1000000000
min_output = 1000000000

res_list= []

def find_result(index, result, add, sub, mul, div):
    if index == N-1:
        res_list.append(result)
    if add:
        find_result(index+1, result+A[index+1], add-1, sub, mul, div)
    
    if sub:
        find_result(index+1, result-A[index+1], add, sub-1, mul, div)
    
    if mul:
        find_result(index+1, result*A[index+1], add, sub, mul-1, div)
    
    if div:
        find_result(index+1, int(result/A[index+1]), add, sub, mul, div-1)
    
find_result(0, A[0], operator[0], operator[1], operator[2], operator[3])

for i in res_list:
    if i>=max_output:
        max_output=i
    if i<=min_output:
        min_output=i

print(max_output)
print(min_output)
