import sys

input = sys.stdin.readline

input_string = input().rstrip()
bomb = input().rstrip()
bomb_length = len(bomb)
stack = []

for char in input_string:
    stack.append(char)

    if stack[-1] == bomb[-1]:
        if "".join(stack[-bomb_length:]) == bomb:
            for _ in range(bomb_length):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")


"""
38. 9935 문자열 폭발 (Gold 4)
    - 이런 문제를 보면 무조건 처음 생각 나는 거는 그냥 브루트포스로 그냥 찾는 방법이지만, 
      당연히 1초 이내에 그만둔다. 당연히 TLE일것을 알고 있기 때문

    - 코드 자체는 어려움 없이 간단하게 구현할 수 있는 수준이지만, 생각하는데 까지가 어려웠다.
      (난이도는 C++이나 java의 문자열 다루기 어려움 때문에 좀 더 어려운것 같다.)
    
    - stack에 한 문자씩 넣어주면서, stack의 top 글자와 bomb의 마지막 글자가 일치하는지를 탐색한다.
      stack의 top을 검사하는 이유는 문자열이 폭발하면서 새로운 문자열을 생성했을때, 다시 폭발 문자열이 생길 수 있기 때문이다. 
    
      이후에 일치한다면, stack top에서 bomb의 길이만큼 문자열을 다시 탐색하고 bomb와 일치하는 문자열이면 
      해당 문자열을 삭제한다.

    - stack / 문자열 공부 더하기~
"""
