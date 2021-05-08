N = int(input())

lst = []

for i in range(N):
	lst.append(int(input()))

a = lst[-1]

result = 1

for i in range(len(lst)-2, -1, -1):
	if lst[i] > a:
		a = lst[i]
		result += 1

print(result)