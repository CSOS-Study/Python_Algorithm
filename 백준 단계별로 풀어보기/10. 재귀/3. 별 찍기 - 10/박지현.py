'''
가운데가 뚫리는 부분(line)은 3짜리 별 배열을 3배수로 늘릴 때
가운데 (' ' * 원하는 공백 수) 만큼을 추가해줘야함.

즉, n=9일 때는 가운데 공백이 3x3으로 있고,
공백을 제외한 영역은 n=3 별 배열의 3배수로 진열됨.
'''

def stars(n): # 3이 들어왔을 때
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix

star = ["***", "* *", "***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)

for i in star:
    print(i)