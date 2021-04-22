N,X = map(int,input().split())
score = [i for i in input().split() if int(i)<X]
print(' '.join(score))