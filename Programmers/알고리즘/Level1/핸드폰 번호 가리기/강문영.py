import re


def solution(phone_number):
    num_pattern = re.compile("[0-9]{4}$")
    last_num = num_pattern.search(phone_number).group()

    return "*" * (len(phone_number) - 4) + last_num

# def hide_numbers(s):
#     return "*"*(len(s)-4) + s[-4:]
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : " + hide_numbers('01033334444'));
