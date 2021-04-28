'''
설탕을 최대한 5kg짜리 봉투에 담아야함
설탕을 봉투에 담은 만큼 입력받은 설탕 무게에서 뺀다. (설탕 = 0이 될때까지)
'''
N,cnt = int(input()), 0

while N >=0 : # N=18이라면, (5kg x 3)개 + 3kg 1개
    if N % 5 == 0: # N이 0kg일 때
        cnt += (N//5) # 5kg짜리 봉투 개수
        print(cnt)
        break
    # 설탕이 5kg 봉투만으로 해결이 안되면 3kg짜리에 담기
    N -=3
    cnt +=1
if N < 0 : print(-1)
