n = 1
loop_c = int(input("반복회수 : "))
squared = int(input("제곱승수 : "))
plus_n = int(input("더해지는 숫자 : "))
squared_list = [i ** squared + plus_n for i in range(1, loop_c + 1)]
result_list = []

for i in range(len(squared_list) + len(squared_list) - 1):
    a = -1
    result = ""
    for j in range(1, n + 1):
        result += (str(squared_list[a]) + "  ")
        if j <= n//2:
            a -= 1
        else:
            a += 1
    result_list.append(result)
    if i >= len(squared_list) - 1:
        n -= 2
    else:
        n += 2

max_len = len(sorted(result_list, key=lambda x : len(x), reverse=True)[0])

for i in result_list:
    print(i.center(max_len))
