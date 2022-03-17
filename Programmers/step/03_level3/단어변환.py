from collections import deque


def check(word1, word2):
    temp = 0

    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            temp += 1

        if temp > 1:
            return False

    if temp != 1:
        return False

    return True


def bfs(begin, target, words):
    q = deque()
    q.append((begin, 0))
    visited = set()
    visited.add(begin)

    while q:
        now, dist = q.popleft()

        if now == target:
            return dist

        for word in words:
            if word not in visited and check(now, word):
                q.append((word, dist + 1))
                visited.add(word)

    return 0


def solution(begin, target, words):
    if target not in set(words):
        return 0

    return bfs(begin, target, words)


# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["cog", "log", "lot", "dog", "dot", "hot"]

### 2
begin = "hit"
target = "wow"
words = ["hot", "dog", "dot", "wow"]
print(solution(begin, target, words))