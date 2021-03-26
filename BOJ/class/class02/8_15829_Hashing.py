l = int(input())
input_str = input()
hash_sum = 0

for idx, c in enumerate(input_str):
    hash_sum += (ord(c)-96) * (31 ** idx)

print(hash_sum % 1234567891)
