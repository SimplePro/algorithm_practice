
# 인접 정점을 저장하는 변수
graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


def dfs_paths(start, end):
    stack = [[start]]  # stack 은 경로를 저장하는 변수이다.
    result = []  # result 는 start 부터 end 까지의 경로를 저장하는 변수이다.
    while stack:
        # current_node 는 현재 노드, path 는 경로를 저장하는 변수이다. stack 의 마지막 인덱스의 값을 빼온다.
        current_node, path = stack[-1][-1], stack.pop()
        if current_node == end:  # 현재 노드가 목표지점이라면
            result.append(path)  # result 에 현재 경로를 추가한다.
        else:
            for m in graph[current_node] - set(path):  # 다시 왔던 길을 제외하고 갈 수 있는 노드로 반복문을 돈다.
                stack.append(path + [m])  # 갈 수 있는 노드를 추가한 경로를 stack 에  추가한다.
    # dfs 알고리즘은 가장 먼저 최단경로를 발견하는 것이 아닐 수 있기 때문에 경로 길이를 기준으로 정렬을 한 후 최단 경로를 반환한다.
    return sorted(result, key=lambda x: len(x))[0]


print(dfs_paths('A', 'F'))