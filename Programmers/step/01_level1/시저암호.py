def solution(s, n):
    rst = ""

    for char in s:
        if char == " ":
            rst += " "
        elif char.isupper():
            if ord(char) + n > 90:
                rst += chr(65 + (ord(char) + n - 91))
            else:
                rst += chr(ord(char) + n)
        elif char.islower():
            if ord(char) + n > 122:
                rst += chr(97 + (ord(char) + n - 123))
            else:
                rst += chr(ord(char) + n)

    return rst


def solution2(string, n):
    rst = ""

    for char in string:
        if char == " ":
            rst += " "
        elif char.isupper():
            rst += chr((ord(char) - ord("A") + n) % 26 + 65)
        elif char.islower():
            rst += chr((ord(char) - ord("a") + n) % 26 + 97)

    return rst


print(solution2("AB", 1))
print(solution2("z", 1))
print(solution2("a B z", 4))
