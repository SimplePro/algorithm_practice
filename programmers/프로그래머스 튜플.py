def solution(s):
    answer = []
    overlap_dict = dict()
    s_list = s[1:-1].split("},")
    for i in range(len(s_list)):
        s_list[i] = s_list[i].replace("}", "").replace("{", "")
        s_list[i] = s_list[i].split(",")
    for i in s_list:
        for j in i:
            if overlap_dict.get(j): overlap_dict[j] += 1
            else: overlap_dict[j] = 1
    sorted_overlap_dict = sorted(overlap_dict.items(), key= lambda x : x[1], reverse=True)
    for i in sorted_overlap_dict: answer.append(i[0])
    answer = list(map(int, answer))
    return answer
