H, M = map(int,input().split())

M -= 45

if M >= 0:
	print(H,M)
elif H == 0:
	print(23,60+M)
else:
	print(H-1,60+M)