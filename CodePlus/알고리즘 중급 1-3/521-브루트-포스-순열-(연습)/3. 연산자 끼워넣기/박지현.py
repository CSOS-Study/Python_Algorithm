import itertools, sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
op = ['+', '-', 'x', '//']

real_op = []
for i,j in zip(op, list(map(int, sys.stdin.readline().split()))):
    real_op.extend([i]*j) #0인 부호는 다 날아감

def result(total, n, op):
    if op == '+': return total+n
    elif op == '-': return total-n
    elif op == 'x': return total*n
    else: return int(total/n) #total//n이랑 결과가 다르니 유의할 것.

total_lst = []
#set으로 중복제거 해줘야함 -> 절반으로 줄어듦.
for i in set(itertools.permutations(real_op, N-1)): #순열을 generator처럼 사용
    total = num[0]
    for j in range(len(i)):
        total = result(total,num[j+1],i[j])
    total_lst.append(total)

print(max(total_lst),min(total_lst),sep='\n')