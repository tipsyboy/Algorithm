import sys

input = sys.stdin.readline


front = list(input().rstrip())
back = []
M = int(input())
for _ in range(M):
    command = input().split()

    if command[0] == "L":
        if front:
            back.append(front.pop())
    elif command[0] == "D":
        if back:
            front.append(back.pop())
    elif command[0] == "B":
        if front:
            front.pop()
    elif command[0] == "P":
        front.append(command[1])

print("".join(front + back[::-1]))


"""
1406. 에디터
    - 빡구현하다가 한 10번 틀린 뒤에 검색 참조 했음..

    - 머리가 띵한 풀이였다. 
      해설은 문자열의 끝을 N, 마지막 커서의 위치를 L이라고 하면
      마지막 커서 L을 기준으로 문자열 index 0~L까지가 front
      뒤에서부터 N~L까지는 back이 된다 
      즉, 커서를 기준으로 문자열을 나눠 놓은 것

    - 마지막에 back은 커서를 기준으로 역순으로 저장되있으므로 반전시켜서 결과 값에 추가한다. 
"""