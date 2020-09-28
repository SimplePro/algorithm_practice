def slice_str(s, n): return [s[i:i+n] for i in range(0, len(s), n)]
def solution(s):
    if len(s) == 1: return 1
    answer_list = []
    for i in range(1, len(s)//2 + 1):
        sliced_str = slice_str(s, i)
        count = 1
        result_str = ""
        for j in range(len(sliced_str)):
            if j < len(sliced_str) - 1:
                if sliced_str[j] == sliced_str[j+1]: count += 1
                elif count != 1: 
                    result_str += (str(count) + sliced_str[j])
                    count = 1
                else: result_str += sliced_str[j]
            else:
                if count != 1: result_str += (str(count) + sliced_str[j])
                else : result_str += sliced_str[j]
        answer_list.append(result_str)
    answer_list = sorted(answer_list, key=lambda x : len(x))
    return len(answer_list[0])
