
# # 1)
# score = input()

# mid = len(score) // 2

# left = 0
# right = 0

# # left
# for i in score[:mid]:
#     left += int(i)

# # right
# for i in score[mid:]:
#     right += int(i)

# if left == right:
#     print("LUCKY")
# else:
#     print("READY")


# 2)
score = input()
summary = 0

for i in range(len(score)//2):
    summary += int(score[i])

for i in range(len(score)//2, len(score)):
    summary -= int(score[i])

if not summary:
    print("LUCKY")
else:
    print("READY")
