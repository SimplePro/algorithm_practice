
# 인접 정점을 저장하는 변수
graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


def bfs_paths(start, end):
    queue = [[start]]  # queue 는 경로를 저장하는 변수이다.

    while queue:  # queue 가 None 이 아닐 때 반복

        # 경로의 현재 노드를 current_node 에 저장하고, path 에 경로가 저장되어 있는 queue 의 0 번째 인덱스에서 빼온다.
        current_node, path = queue[0][-1], queue.pop(0)
        if current_node == end:  # 현재 노드가 목표지점이라면
            return path  # 최단 경로를 반환한다.

        else:  # 현재 노드가 목표지점이 아니라면
            for m in graph[current_node] - set(path):  # 다시 왔던 길을 제외하고 갈 수 있는 노드로 반복문을 돈다.
                queue.append(path + [m])  # 갈 수 있는 노드를 추가한 경로를 queue 에 추가한다.

    return "원하는 목표지점에 갈 수 없습니다."  # 반복문을 다 돌 때까지 경로를 찾지 못했다면 갈 수 없다는 문구를 반환.


print(bfs_paths('A', 'F'))