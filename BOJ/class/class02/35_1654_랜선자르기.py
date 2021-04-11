import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

rst = []


def cut_lan(lan, n, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    # # 랜선의 최소길이가 1이므로 필요가 없다. (함수 호출 때, start 값을 1로 시작)
    # if mid == 0:
    #     # rst.append(1)
    #     return
    lines = 0
    for la in lan:
        lines += la // mid

    if lines >= n:
        rst.append(mid)
        cut_lan(lan, n, mid + 1, end)
    else:
        cut_lan(lan, n, start, mid - 1)


cut_lan(lan, n, 1, max(lan))
print(max(rst))
