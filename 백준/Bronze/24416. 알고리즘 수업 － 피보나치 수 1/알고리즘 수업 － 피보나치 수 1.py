import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

f1_calls = 0
f2_calls = 0

def f1(n):
    global f1_calls
    f1_calls += 1
    if n == 1 or n == 2:
        return 1
    else:
        return f1(n-1) + f1(n-2)

def f2(n):
    global f2_calls
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1): 
        f2_calls += 1 
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

N = int(input())

f1_result = f1(N)
f2_result = f2(N)

print(f1_result,f2_calls)