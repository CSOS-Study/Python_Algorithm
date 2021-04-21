n = int(input())

def extract_ratio(student_score):
    avg = sum(student_score[1:]) / student_score[0]
    cnt = 0
    for i in student_score[1:]:
        if (i > avg):
            cnt += 1
    return cnt

for _ in range(n):
    student_score= list(map(int,input().split()))
    print("{:.3f}%".format(extract_ratio(student_score)/student_score[0]*100))