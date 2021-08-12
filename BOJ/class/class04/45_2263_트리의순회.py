import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def get_preorder(in_start, in_end, post_start, post_end):
    # 리스트 값이 하나만 남은 경우에도 탐색해야하기 때문
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]  # 분할된 현재 트리의 루트
    preorder_traversal.append(str(root))  # Root Left Right
    idx = inorder_idx[root]  # 트리의 좌/우측을 나누기 위한 inorder의 idx

    # 트리의 좌/우측 노드의 개수
    left_length = idx - in_start
    right_length = in_end - idx

    # Left 탐색
    get_preorder(in_start, idx - 1, post_start, post_start + left_length - 1)
    # Right 탐색
    get_preorder(idx + 1, in_end, post_end - right_length, post_end - 1)


n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorder_idx = [0] * (n + 1)  # inorder의 index 저장
preorder_traversal = []  # 결과 값 - 전위 순회

for i in range(n):
    inorder_idx[inorder[i]] = i

get_preorder(0, len(inorder) - 1, 0, len(postorder) - 1)

print(" ".join(preorder_traversal))

"""
45. 2263 트리의 순회 (Gold 3)
    - 금방 할 수 있을줄 알았는데 정말 오래 걸렸던 문제.. 
      처음 구현부터 python 재귀 깊이 실수, idx에러, return 지점, TLE까지 우여곡절이 많았다. 

    - 기본적으로 트리의 순회(전위/중위/후위)에 대한 내용이다. 

    1.
    - post_order의 마지막 노드는 전체 트리의 루트가 되고 간선을 잘라도 또 다른 트리가 되는 트리의 특성상
      left/right로 나눈 서브트리도 마지막 노드가 서브트리의 루트가 된다.
    2. 
    - post_order에서 찾는 root를 기준으로 in_order의 좌측은 left 서브트리 우측은 right 서브트리가 된다. 
    3.
    - 위의 특징을 살려서 index를 나누면 분할정복으로 pre_order를 구할 수 있다. 
    4.
    - 재귀적으로 문제를 풀때 파이썬은 재귀 깊이를 늘려주자.
    5.
    - in_order의 root index를 찾는데 index() 함수를 사용했는데, TLE를 받았고 
      미리 index 값을 역으로 저장하는 리스트를 하나 생성해서 해결하였다. 
    
    6. ****** 중요 ******
    - 이런 분할정복이나 dp문제를 풀때는 항상 예시문을 미지의 n번째 상황이라고 생각하고 풀자.
"""

"""
test case

12
8 4 2 5 9 1 10 6 11 3 7 12
8 4 9 5 2 10 11 6 12 7 3 1
"""