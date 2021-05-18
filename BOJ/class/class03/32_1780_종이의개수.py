import sys
input = sys.stdin.readline


def check_paper(x, y, length):
    flag = paper[x][y]

    # check the paper from start loc to end loc
    for i in range(length):
        for j in range(length):
            if flag != paper[x + i][y + j]:
                return False

    return True


def cut_paper(x, y, length):  # tree start loc (x, y) = (row, col), paper length
    global rst

    # 1) length == 1
    if length == 1:
        rst[paper[x][y] + 1] += 1

        return

    # 2) check the paper
    if check_paper(x, y, length):
        rst[paper[x][y] + 1] += 1
    else:  # 2-1) if check value is False, cut the paper
        for i in range(3):
            for j in range(3):
                cut_paper(x + length//3*i, y + length//3*j, length//3)


# input paper data
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
rst = [0, 0, 0]  # -1, 0, 1
# dict를 사용해서 rst 값을 저장하면, global로 리스트를 들고 다니지 않아도 되더라?
dic = {-1: 0, 0: 0, 1: 0}

cut_paper(0, 0, n)
print(rst[0])
print(rst[1])
print(rst[2])
