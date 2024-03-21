#틀린 이유: for 써서 완전 탐색했음
#해결 방안: 투 포인터를 사용할 것

N, S = map(int,input().split())

num_list = list(map(int, input().split()))

left = 0
right = 1

temp = num_list[0]
length = 100001

while True:
    if temp >= S:
        length = min(length, right - left) #넘었으면 길이 재야지
        temp -= num_list[left] #왼쪽꺼 오른쪽으로 돌려
        left += 1

    elif right == N:
        break

    else:
        temp += num_list[right]
        right += 1

if length == 100001:
    print(0)

else:
    print(length)
