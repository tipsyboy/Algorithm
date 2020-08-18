x_coord = int(input())
y_coord = int(input())

if x_coord > 0:
    if y_coord > 0:
        print("1")
    else:
        print("4")
else:
    if y_coord > 0:
        print("2")
    else:
        print("3")
