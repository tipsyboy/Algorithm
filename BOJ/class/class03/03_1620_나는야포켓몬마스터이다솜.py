import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 도감의 포켓몬 수, 맞추기
pokedex_dict = dict()  # 도감
pokedex_list = []

for i in range(n):
    pokemon = input().strip()
    pokedex_list.append(pokemon)
    pokedex_dict[pokemon] = i + 1


for _ in range(m):
    command = input().strip()

    if command.isdigit():
        print(pokedex_list[int(command) - 1])
    else:
        print(pokedex_dict[command])
