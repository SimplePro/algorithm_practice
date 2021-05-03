# --------------------------- first method ---------------------------
# n = int(input())

# def solution(n):
#   ns = ['1']
#   remainder = []

#   m = 0

#   while True:
#     if int(ns[-1]) % n == 0:
#       m = int(ns[-1])
#       break

#     if (int(ns[-1]) % n) in remainder:
#       m = int(ns[-1]) - int(ns[remainder.index(int(ns[-1]) % n)])
#       break

#     remainder.append(int(ns[-1]) % n)
#     ns.append(ns[-1] + "1")

#   result = n
#   while result <= m:
#     if str(result).count("1") + str(result).count("0") == len(str(result)):
#       print(result)
#       break

#     result += n

# for i in range(31, n+1):
#   solution(i)

# ------------------------------- second method ---------------------------------
# from queue import Queue
# from time import time

# n = int(input())

# start_time = time()

# def bfs(n):
#   visit = {}
#   queue = Queue()
#   queue.put("1")

#   cnt = 0
#   while queue or cnt >= 100000000:
#     if time() - start_time >= 0.9: return 0

#     node = queue.get()

#     if int(node) % n == 0: return node

#     visit[node] = True
#     queue.put(node + "0")
#     queue.put(node + "1")

#     cnt += 1
    
#   return 0

# if str(n).count("1") + str(n).count("0") == len(str(n)):
#   print(n)

# elif n % 10 == 0:
#   a = n // 10
#   cnt = 0
#   while True:
#     if a % 2 == 0:
#       cnt += 1
#       a //= 2
#     else: break

#   print(10**(cnt+1)*int(bfs(n//10//(2**cnt))))

# else:
#   a = n
#   cnt = 0
#   while True:
#     if a % 2 == 0:
#       cnt += 1
#       a //= 2

#     else: break

#   print((10**cnt) * int(bfs(n//(2**cnt))))


# --------------------- third method ---------------------
# def zero_one(x): return str(x).count("1") + str(x).count("0") == len(str(x))

# n = int(input())

# multiple_list = [n*i for i in range(1, 10)]

# result = 0

# for i in multiple_list:
#   if str(i)[-1] == "1" or str(i)[-1] == "0":
#     result = i
#     break

# for i in range(1, n + 1):
#   if zero_one(result): break

#   for j in multiple_list:
#     a = result + 10**i * j  # 이전값 + n * a(i)
#     digit = str(a)[-(i+1)]  # 해당 자리 숫자
#     m = a + 10**(i) * multiple_list[-1]  # 수가 너무 작아 성립이 안되는 경우를 막기 위한 값

#     if zero_one(a) or (m >= 10**(i+2) and (digit == "1" or digit == "0")):
#       result = a
#       break

# print(result)
