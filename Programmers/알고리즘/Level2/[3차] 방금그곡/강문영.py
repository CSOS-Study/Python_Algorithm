import re


# 악보 내에서 연속된 비교가 이뤄져야 함
# 연속된 비교가 이뤄진 후에도 더 긴 연주를 하는 경우에만 제외를 시켜야함 

def change(melody):
    if 'A#' in melody: melody = melody.replace('A#', 'a')
    if 'C#' in melody: melody = melody.replace('C#', 'c')
    if 'D#' in melody: melody = melody.replace('D#', 'd')
    if 'F#' in melody: melody = melody.replace('F#', 'f')
    if 'G#' in melody: melody = melody.replace('G#', 'g')
    return melody


def solution(m, musicinfos):
    m = change(m)
    answer = ('(None)', None)
    for musicinfo in musicinfos:
        music_start, music_end, title, sheet = musicinfo.split(",")
        music_play_time = (int(music_end.split(":")[0]) - int(music_start.split(":")[0])) * 60 + (
                    int(music_end.split(":")[1]) - int(music_start.split(":")[1]))
        sheet = change(sheet)
        music_play_list = ''.join([sheet[i % len(sheet)] for i in range(music_play_time)])

        if m in music_play_list:
            if (answer[1] == None) or music_play_time > answer[1]:
                answer = (title, music_play_time)

    return answer[0]