from bisect import bisect_right

def solution(d, budget):
    answer = 0
    process = []
    plus = 0
    sorted_d = sorted(d)
    for i in sorted_d:
        plus += i
        process.append(plus)
    return bisect_right(process, budget)
