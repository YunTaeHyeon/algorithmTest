N, K = map(int, input().split())
words = []
alpha = []
res = 0

for i in range(N):

    word = input()
    one_word = []

    for w in word:
        if w not in alpha:
            if w != 'a' and w != 'n' and w != 't' and w != 'i' and w != 'c':
                alpha.append(w) #중복되지 않는 녀석들만
        if w != 'a' and w != 'n' and w != 't' and w != 'i' and w != 'c':
            one_word.append(w)
        
    words.append(one_word)

print(alpha)

print()
print(words)

if K == 5:
    for w in range(words):
        if 'a' not in 'a' and w != 'n' and w != 't' and w != 'i' and w != 'c':
            print(0)
        else:
            print(1)
elif K < 5:
    print(0)

else:
    max_res = 0
    #i를 지웠을 때 다 지워진거면 1개 추가
    for count in K-5:
        for i in range(alpha):
            for j in range(len(words)):
                if i == words[j]:
                    words[j].remove(i)
                    if len(words[j]) == 0:
                        res += 1
        
