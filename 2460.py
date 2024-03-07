count = 0
res = []

for _ in range(10):
    o,i = map(int, input().split())
    count = count - o + i

    res.append(count)

max = 0

for i in range(len(res)):
    if res[i] > max:
        max = res[i]

print(max)

