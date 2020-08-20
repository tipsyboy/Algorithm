import sys

init_x = int(sys.stdin.readline())
rst = init_x
count = 0

while True:
    count += 1
    rst = (rst % 10)*10 + ((rst//10 + rst % 10) % 10)
    # print(f"init_x: {init_x}, rst: {rst}")
    if init_x == rst:
        break

print(count)
