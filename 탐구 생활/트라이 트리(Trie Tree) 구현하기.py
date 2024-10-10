"""
# Last Modified. 2024.10.10 THU
# 트라이 트리(Trie Tree) 구현하기.py

"""


# Node class
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


# Trie class
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head  # Node pointer를 head로 설정

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]  # Node 포인터를 이동

        current_node.data = string  # 단어를 저장함.

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True


trie = Trie()  # 객체 생성
words = ["frodo", "front", "firefox", "fire"]

for word in words:
    trie.insert(word)

print(trie.search("friend"))
print(trie.search("frodo"))
print(trie.search("fire"))
