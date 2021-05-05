k = int(input())
g = list(map(int, input().split()))
S = sum(g)
gs = [0 for i in range(S)]

def dfs(depth, x):
    global gs
    if depth == len(g) and x > 0 and x <= S: gs[x-1] = 1
    elif depth != len(g):
        dfs(depth+1, x+g[depth])
        dfs(depth+1, x-g[depth])
        dfs(depth+1, x)

dfs(0, 0)

print(gs.count(0))