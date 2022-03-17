def solution(progresses, speeds):
    stack = progresses[::-1]
    speeds = speeds[::-1]
    rst = []

    while stack:
        for i in range(len(stack)):
            stack[i] += speeds[i]

        count = 0
        while stack and stack[-1] >= 100:
            count += 1
            stack.pop()
            speeds.pop()

        if count:
            rst.append(count)

    return rst


progresses = [93, 30, 55]
speeds = [1, 30, 5]
solution(progresses, speeds)