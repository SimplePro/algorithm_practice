def solution(progresses, speeds):
    answer = []
    perfection_count = []
    for i in range(0, len(progresses)):
        count = 0
        perfection = progresses[i]
        while True:
            if not perfection >= 100:
                perfection += speeds[i]
                count += 1
                continue
            perfection_count.append(count)
            break
    work = 1
    count = 0
    current_number = perfection_count[0]
    small_number = 0
    while True:
        try:
            if current_number < perfection_count[count+1]:
                current_number = perfection_count[count+1]
                answer.append(work)
                work = 1
            else: work += 1
            count += 1
        except:
            answer.append(work)
            break
    return answer
