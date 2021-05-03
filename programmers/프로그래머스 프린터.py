def solution(priorities, location):
    order_list = [0 for _ in range(len(priorities))]
    order = sorted(priorities, reverse=True)
    cnt = 1
    n = 0
    while 0 in order_list:
        if n >= len(priorities): n = 0
        if priorities[n] == order[0]:
            order_list[n] = cnt
            cnt += 1
            del order[0]
        n += 1
    return order_list[location]
