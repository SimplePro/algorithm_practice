from bisect import bisect_left, bisect_right
from time import time

n, k = map(int, input().split())

# hamburger = 0, persone = 1
H_P = list((map(int, list(input().replace("H", "0").replace("P", "1")))))

start_time = time()

H_index = []
P_index = []

for i in range(len(H_P)):
    if H_P[i] == 0: H_index.append(i)
    else: P_index.append(i)


result = 0

h, p = 0, 0

while h < len(H_index) or p < len(P_index):
    try:
        if abs(P_index[p] - H_index[h]) <= k: result += 1; p += 1; h += 1
        elif P_index[p] - H_index[h] > k: h += 1
        elif abs(P_index[p] - H_index[h]) > k: p += 1
    except: break

print(result)