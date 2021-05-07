going, slide, height = map(int, input().split())

k = (height - slide)/(going-slide)
print(int(k) if k == int(k) else int(k)+1)

