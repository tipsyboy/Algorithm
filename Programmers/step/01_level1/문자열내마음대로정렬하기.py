def solution(strings, n):
    rst = sorted(strings)
    rst = sorted(rst, key=lambda x: x[n])

    return rst


# solution(["sun", "bed", "car"], 1)
solution(["abce", "abcd", "cdx"], 2)
