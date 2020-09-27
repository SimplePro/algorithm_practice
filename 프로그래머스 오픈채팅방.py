def solution(record):
    answer = []
    name_dict = dict()
    action_list = []
    for i in record:
        record_list = i.split()
        if record_list[0] == "Enter":
            action_list.append("Enter,"+record_list[1])
            name_dict[record_list[1]] = record_list[2]
        elif record_list[0] == "Change": name_dict[record_list[1]] = record_list[2]
        elif record_list[0] == "Leave": action_list.append("Leave,"+record_list[1])
    for i in action_list:
        action, uid = i.split(",")
        if action == "Enter": answer.append(name_dict[uid]+"님이 들어왔습니다.")
        if action == "Leave": answer.append(name_dict[uid]+"님이 나갔습니다.")
    return answer
