"""
    - 십진수 -> {base}진수로 변환 
    
    - 나머지 String(T)을 정의해놓고 나머지를 붙여 나간다.
"""


def convert_numeral_system(number: int, base: int) -> str:
    T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    q, r = divmod(number, base)
    return convert_numeral_system(q, base) + T[r] if q else T[r]

    # if q == 0:
    #     return T[r]
    # else:
    #     return convert_numeral_system(q, base) + T[r]


N, B = map(int, input().split())
print(convert_numeral_system(N, B))