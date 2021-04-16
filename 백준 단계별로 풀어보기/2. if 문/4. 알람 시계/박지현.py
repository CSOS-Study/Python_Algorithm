H,M=map(int, input().split())

if M<45:
    H-=1
    M=60-(45-M)
    if H<0:
        print(23,M,sep=' ')
    else:
        print(H,M,sep=' ')
else:
    print(H,M-45, sep=' ')