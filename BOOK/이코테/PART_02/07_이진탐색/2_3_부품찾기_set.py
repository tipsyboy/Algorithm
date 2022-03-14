n = int(input())
arr = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for part in x:
    if part in arr:
        print("yes", end=" ")
    else:
        print("no", end=" ")
