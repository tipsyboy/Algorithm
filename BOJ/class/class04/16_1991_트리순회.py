import sys
input = sys.stdin.readline


# 1) dict안에 dict 이용하기
def preorder(tree, node):
    print(node, end="")

    if tree[node]["left"] != ".":
        preorder(tree, tree[node]["left"])

    if tree[node]["right"] != ".":
        preorder(tree, tree[node]["right"])


def inorder(tree, node):
    # if tree[node]["left"] == "." and tree[node]["right"] == ".":
    #     print(node, end="")
    #     return

    if tree[node]["left"] != ".":
        inorder(tree, tree[node]["left"])

    print(node, end="")

    if tree[node]["right"] != ".":
        inorder(tree, tree[node]["right"])


def postorder(tree, node):
    # if tree[node]["left"] == "." and tree[node]["right"] == ".":
    #     print(node, end="")
    #     return

    if tree[node]["left"] != ".":
        postorder(tree, tree[node]["left"])

    if tree[node]["right"] != ".":
        postorder(tree, tree[node]["right"])

    print(node, end="")


n = int(input())
tree = dict()

for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = {"left": left, "right": right}

print(tree)
preorder(tree, "A")
print()
inorder(tree, "A")
print()
postorder(tree, "A")
print()


# # 2) dict의 value인 Node 값은 class로 선언해보기
# class Node:
#     def __init__(self, root, left, right):
#         self.root = root
#         self.left = left
#         self.right = right


# def preorder(node):
#     print(node.root, end="")

#     if node.left != ".":
#         preorder(tree[node.left])

#     if node.right != ".":
#         preorder(tree[node.right])


# def inorder(node):
#     if node.left != ".":
#         inorder(tree[node.left])

#     print(node.root, end="")

#     if node.right != ".":
#         inorder(tree[node.right])


# def postorder(node):
#     if node.left != ".":
#         postorder(tree[node.left])

#     if node.right != ".":
#         postorder(tree[node.right])

#     print(node.root, end="")


# n = int(input())
# tree = dict()
# for _ in range(n):
#     root, left, right = map(str, input().split())
#     tree[root] = Node(root, left, right)

# preorder(tree["A"])
# print()
# inorder(tree["A"])
# print()
# postorder(tree["A"])
# print()


"""
16. 1991 트리 순회 (Silver 1):
    - 트리 자료구조, 재귀함수 문제
    
    1) 첫 번째 풀이 
    - 입력 받는 노드의 개수가 크지 않기 때문에 dict()로 선언하고 이진트리 특성을 이용해서 
      left, right 값만 다시 dict로 추가해줬다. 트리를 차례로 순회 하면서 left, right 값이 없는 경우는 넘어가고
      있는 경우 재귀로 호출해 주는 방식으로 해결했다. 
    
    - 전위/중위/후위식은 정보처리기사 이후로 가물가물 했는데, 문제에서 탐색 순서가 나와 있어서 어렵지 않게
      다시 떠올려서 해결할 수 있었다.

    2) 두 번째 풀이
    - 1)번 풀이에 dict안에 dict를 넣는 것을 그냥 Node class를 선언해서 바꿔 줬을 뿐이다.
"""
