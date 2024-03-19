T = int(input())

for _ in range(T):
    n = int(input())

    answer = []

    while True:
        if n == 0:
            break

        answer.append(n%2)
        n = n//2

    for i in range(len(answer)):
            if answer[i] == 1:
                print(i, end = ' ')

    print()