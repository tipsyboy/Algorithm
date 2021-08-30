import sys

input = sys.stdin.readline


input_string = input().rstrip()
char_list = []
sum_value = 0
count = 0  # 숫자가 등장한 횟수

for char in input_string:
    if char.isalpha():
        char_list.append(char)
    else:
        count += 1
        sum_value += int(char)

char_list.sort()

if count != 0:
    char_list.append(str(sum_value))

print("".join(char_list))

"""
08. 문자열 재정렬
    - 이 문제의 경우 숫자가 0~9로 구성되어 있는데, 0만 등장한 경우가 있을 수 있어서 
      숫자가 등장한 횟수를 count로 세주는 것으로 변경해서 다시 작성했다.
"""