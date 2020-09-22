# # -> 소문자
def replace_sharp(s):
    return s.replace("A#", "a").replace("C#", 'c').replace("D#", 'd').replace("F#", 'f').replace("G#", 'g')

# 재생 시간 추출
def extraction_minutes(start_time, end_time):
    minute = 0
    hour = 1 * (int(end_time.split(':')[0]) - int(start_time.split(':')[0]))
    if hour == 0: minute = int(end_time.split(':')[1]) - int(start_time.split(':')[1])
    else: minute = 60 * hour + int(end_time.split(':')[1]) - int(start_time.split(':')[1])
    return minute

# 재생 시간 만큼 멜로디 추출
def extraction_melody(melody, duration):
    melody = replace_sharp(melody)
    melody = melody*(duration // len(melody)+1)
    return melody[:duration]

def solution(m, musicinfos):
    m = replace_sharp(m)
    play_time = [0]
    play_title = ['(None)']
    for music in musicinfos:
        start_time, end_time, title, melody = music.split(',')
        duration = extraction_minutes(start_time, end_time)
        melody = extraction_melody(melody, duration)
        if m in melody:
            play_time.append(duration)
            play_title.append(title)
    return play_title[play_time.index(max(play_time))]
