N, K = map(int, input().split())
words = []
res = 0
alpha=[]

for i in range(N):

    alpha_in_words=[]

    word = input()
    for w in word:
        if w != 'a' and w != 'n' and w != 't' and w != 'i' and w != 'c':
            alpha_in_words.append(w)
            if w not in alpha:
                alpha.append(w)
    
    words.append(alpha_in_words)

print(words)
print(alpha)

def find(num):
    if num == 0:

    
    

    
 