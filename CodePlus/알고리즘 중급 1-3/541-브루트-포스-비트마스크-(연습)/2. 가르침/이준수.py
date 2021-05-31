#고를 수있는 인덱스.
#학습된 결과와 word와의 and연산이 word와 같다면 해당 word는 학습으로 읽을 수 있는 단어이다.
#현재알파벳, 가르친 단어수, 가르친 단어(bit)
def dfs(alphabet, learned_N, learned):
    #가르친 단어수가 K인 경우.
    if(learned_N == K):
        #가르친 단어수에 따른 읽을수있는 단어수를 계산한다.
        cnt = 0
        for word in words:
            if word == (word & learned):
                cnt += 1
        return cnt

    #가르쳐야할 단어의 수가(K - learned_N). 현재 알파벳을 포함해서
    #남은 알파벳 수보다 많다면 -1을 리턴한다.
    #이거 안해주면 시간초과. 아마 생각외로 함수의 갯수를 많이 줄여주는것같음.
    if(K - learned_N > 26 - alphabet):
        return -1

    #알파벳이 Z를 넘어가면 선택 불가능하다.
    if(alphabet == 26):
        return -1

    #이미 가르친 경우 다음으로 넘어간다.
    if(learned_N & (1 << alphabet) == alphabet):
        return dfs(alphabet+1, learned_N, learned)

    #현재 알파벳을 가르치는 경우 / 가르치지 않는 경우
    return max(dfs(alphabet+1, learned_N+1, learned | (1 << alphabet)), dfs(alphabet+1, learned_N, learned))


N, K = map(int, input().split())

#word를 비트로 표현한다.
words = []
for _ in range(N):
    word = 0
    for char in input():
        word |= 1 << (ord(char)-ord('a'))
    words.append(word)

#학습된 결과이다.
learn = 0
#a,n,t,i,c 을 학습시킨다.
learn |= 1 << (ord('a')-ord('a'))
learn |= 1 << (ord('n')-ord('a'))
learn |= 1 << (ord('t')-ord('a'))
learn |= 1 << (ord('i')-ord('a'))
learn |= 1 << (ord('c')-ord('a'))

if K == 26:#K가 26이라면, 모든 영단어를 다 읽을수있는 것이다.
    print(N)
elif K < 5:#K가 5미만이라면, 모든 영단어를 다 읽을수없는 것이다.
    print(0)
else:#이외의 경우 브루트포스를 통해서 결과를 구한다.
    print(dfs(0, 5, learn))


#https://ooyoung.tistory.com/104
#https://onlytrying.tistory.com/154














'''
import re

def count_bit(n):
    return n % 2 + count_bit(n // 2) if n >= 2 else n

N, K = map(int, input().split())
words = [set(re.findall(r'[^acnit]',input())) for _ in range(N)]
union_words = set()
for word in words:
    union_words |= word

if K < 5:
    print(0)
    exit()

K = K - 5
word_n = len(union_words)
union_words = list(union_words)

#K는 최대로 배울수있는 단어수이다. 만약에 배워야하는 단어의수가 K보다 같거나 작으면 모든 단어를 배울수있다는뜻이다.
if K >= word_n:
    print(len(words))
    exit()

#최대로 배울수있는 단어의 수만큼 배운다.
res = 0
for i in range(1 << word_n):
    if count_bit(i) == K:
        choosen_alpha = set()
        for j in range(word_n):
            if i & 1 << j:
                choosen_alpha.add(union_words[j])
        cnt = 0
        for word in words:
            if word == word & choosen_alpha:
                cnt += 1
        res = max(res, cnt)

print(res)
'''
