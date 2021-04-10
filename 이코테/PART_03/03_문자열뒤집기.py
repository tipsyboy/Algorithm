input_str = input()
s_dict = {'0': 0, '1': 0}

now = input_str[0]

for s in input_str[1:]:
    if now != s:
        s_dict[now] += 1
        now = s

s_dict[now] += 1

print(s_dict)
print(min(s_dict.values()))
