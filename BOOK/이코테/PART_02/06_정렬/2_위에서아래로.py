n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

lst = sorted(lst, reverse=True)

print(lst)
