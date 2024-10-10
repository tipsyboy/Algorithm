"""
# Last Modified. 2024.10.10 THU
# 진수 변환 함수를 구현해보자

- 십진수 -> {base}진수로 변환 
    
- 나머지 String(T)을 정의해놓고 나머지를 붙여 나간다.
"""


def base_converter(number, base):
    D = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 진수 변환시 필요한 문자 매핑

    q, r = divmod(number, base)
    return base_converter(q, base) + D[r] if q else D[r]

    # if q == 0:
    #     return T[r]
    # else:
    #     return base_converter(q, base) + D[r]


N, B = map(int, input().split())
print(base_converter(N, B))
