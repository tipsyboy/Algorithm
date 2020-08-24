
# 귀찮음이 가장 빠른 길일때도 있다.
import sys

words = sys.stdin.readline()
dial_time = 0

for word in words[:-1]:
    if word in ["A", "B", "C"]:
        dial_time += 3
    elif word in ["D", "E", "F"]:
        dial_time += 4
    elif word in ["G", "H", "I"]:
        dial_time += 5
    elif word in ["J", "K", "L"]:
        dial_time += 6
    elif word in ["M", "N", "O"]:
        dial_time += 7
    elif word in ["P", "Q", "R", "S"]:
        dial_time += 8
    elif word in ["T", "U", "V"]:
        dial_time += 9
    elif word in ["W", "X", "Y", "Z"]:
        dial_time += 10

print(dial_time)
