for h, w, n in [map(int, input().split()) for _ in range(int(input()))]:
    print('{0}{1:02d}'.format((n % h if n % h else h), ((n // h) + 1) if n % h else n // h))
