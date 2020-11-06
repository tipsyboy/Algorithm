# # ##### O(n^2) 알고리즘 연습 #####
# # 1. 선택 정렬
# x = [9, 1, 6, 8, 4, 3, 2, 0]

# print("##### 선택 정렬 #####")
# print(f"초기값: {x}")
# for i in range(len(x)-1):
#     min_idx = i

#     for j in range(i+1, len(x)):
#         if x[min_idx] > x[j]:
#             min_idx = j

#     print(f"{x} -> ", end="")
#     x[i], x[min_idx] = x[min_idx], x[i]  # swap
#     print(f"{x}")
# print(f"결과: {x}")

# # 2. 삽입 정렬
