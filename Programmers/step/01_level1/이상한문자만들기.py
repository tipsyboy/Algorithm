def solution(s):
    string = s.split(" ")
    rst = []

    for word in string:
        temp = list(word)
        for i in range(len(temp)):
            if i % 2 == 0:
                temp[i] = temp[i].upper()
            else:
                temp[i] = temp[i].lower()

        rst.append("".join(temp))

    return " ".join(rst)


print(solution("try hello world"))
