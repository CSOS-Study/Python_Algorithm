import re

special_char_pattern_2 = '[^a-z0-9-_.]+'  ## 알파벳 소문자, 숫자, 빼기, 밑줄 , 마침표
dot_pattern_3 = '\\.{2,}'
first_dot_pattern_4 = '^\\.'
last_dot_pattern_4 = '\\.$'


def solution(new_id):
    global special_char_pattern_2
    global dot_pattern_3
    global first_dot_pattern_4
    global last_dot_pattern_4
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = re.sub(special_char_pattern_2,'',new_id)
    # 3단계
    new_id = re.sub(dot_pattern_3,'.',new_id)
    # 4단계
    new_id = re.sub(first_dot_pattern_4,'',new_id)
    new_id = re.sub(last_dot_pattern_4,'',new_id)
    # 5단계
    if len(new_id) ==0:
        new_id = 'a'
    # 6단계
    if len(new_id)>=16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7단계
    while(len(new_id)<3):
        new_id = new_id + new_id[-1]

    return new_id

# 스고이 .. 
# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st