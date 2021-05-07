n = int(input())

def pibonachi(n):
    if n<=1:
        return n
    return pibonachi(n-1) + pibonachi(n-2)

print(pibonachi(n))