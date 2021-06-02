def dfs(alphabet, learned_N, learned):
    # 읽을수있는 단어의 개수를 계산한다.
    '''
    현재 학습한 단어가 a,n,t,i,c,r,z,h라면,
    learned = 10000010100010000110000101
    for문에서 word가 antartica라면,
    word = 00000010100010000100000101
    word & learned 연산 하면 word가 그대로 나온다.
    즉, 이럴 경우 word에 대한 모든 알파벳이 학습되었으므로 word를 읽을 수 있다.
    '''
    if(learned_N == K):
        cnt = 0
        for word in words:
            if word == (word & learned): #해당 단어(word)를 읽을 수 있다는 것
                cnt += 1
        return cnt

    # alphabet이 a부터 z까지 순서대로 재귀를 돌면서 모든 알파벳의 학습 여부를 확인하는데,
    # 만약 앞으로 가르쳐야하는 알파벳의 개수(K-learned_N)가 남은 alphabet보다 많다면
    # 진행 불가능이므로 -1을 return한다.
    # ex) alphabet = y 즉, 남은 alpha가 z일 때 K-learned_N > 1이면 노답인 것
    if(K - learned_N > 26 - alphabet):
        return -1

    #알파벳이 Z를 넘어가면 더이상 진행 불가능
    if(alphabet == 26):
        return -1

    if(learned_N & (1 << alphabet) == alphabet): # alphabet을 이미 가르친 상태라면
        return dfs(alphabet+1, learned_N, learned) # 다음 알파벳을 가르치기 위해 재귀를 돈다.

    #현재 알파벳을 가르치는 경우 / 가르치지 않는 경우
    return max(dfs(alphabet+1, learned_N+1, learned | (1 << alphabet)), dfs(alphabet+1, learned_N, learned))
    #가장 많은 단어를 읽을 수 있는 경우를 찾는다.

N, K = map(int, input().split())
words = []
for _ in range(N):
    word = 0
    for char in input(): #단어를 입력받는다.
        word |= 1 << (ord(char)-ord('a'))
    words.append(word) #각 단어를 words 에 저장한다.

learned = 0
#a,n,t,i,c 을 학습시킨다.
learned |= 1 << (ord('a')-ord('a'))
learned |= 1 << (ord('n')-ord('a'))
learned |= 1 << (ord('t')-ord('a'))
learned |= 1 << (ord('i')-ord('a'))
learned |= 1 << (ord('c')-ord('a'))
#a,n,t,i,c가 학습된 learned가 완성된다.
#learned = 10000010000100000101 ( = 532741 )

if K == 26:#모든 영단어를 다 읽을수있다.
    print(N)
elif K < 5:#모든 영단어를 다 읽을수없다.
    print(0)
else:
    print(dfs(0, 5, learned)) # 0은 a를 의미 -> a부터 전부 다 돌거니까