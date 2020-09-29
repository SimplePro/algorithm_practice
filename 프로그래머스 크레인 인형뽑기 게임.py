def solution(board, moves):
    answer = 0
    last_basket_num = -1
    basket = [-1]
    for i in moves:
        layer = 0
        if board[-1][i-1] == 0: continue
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                layer = j
                break
        if board[layer][i - 1] == last_basket_num:
            del basket[-1]
            answer += 2
        else: basket.append(board[layer][i-1])
        last_basket_num = basket[-1]
        board[layer][i - 1] = 0
    return answer
