N, K = map(int,input().split())
todo = list(map(int,input().split()))

count = 0
plug = []

for i in range(len(todo)):
    if todo[i] in plug:
        continue
    if len(plug) < N:
        plug.append(todo[i])
    else:
        #가장 많이 사용될 제품 선정
        max_idx = -1 #가장 마지막 사용 위치
        max_val = -1 #가장 마지막 사용 시점
        for j in range(N):
            if plug[j] not in todo[i:]:
                max_idx = j
                break
            else: #위치를 파악하고 가장 마지막에 사용할 것으로 바꿈
                idx = todo[i:].index(plug[j]) 
                if idx > max_val:
                    max_val = idx
                    max_idx = j
        plug[max_idx] = todo[i]             
        count += 1

print(count)

    
