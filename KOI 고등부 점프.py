from bisect import bisect_right

frog = []
k = 1
up = 1
for i in range(50):
  frog.append(k)
  up *= 2
  k += up

def extract_n(x):
  up = 0.5
  jump_n = bisect_right(frog, x)
  d = x - frog[jump_n-1]

  while d != 0:
    up *= 2
    if d == up:
      jump_n += 1
      break
    elif d > up: d -= up
    elif d < up:
      up = 1
      d -= up
    jump_n += 1
  return jump_n

n = int(input())
data = []
result = []
for i in range(n):
  data.append(tuple(map(int, input().split())))
for i in data:
  s, e = i
  lst = []
  for j in range(s, e+1):
    lst.append(extract_n(j))
  result.append(max(lst))

for i in result:
  print(i)
