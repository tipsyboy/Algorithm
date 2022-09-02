import sys

input = sys.stdin.readline


class Item:
    def __init__(self, item_type: str, value: str) -> None:
        self.item_type = item_type
        self.value = value


class Monster:
    def __init__(self, name: str, att: int, defn: int, hp: int, exp: int) -> None:
        self.name = name
        self.att = att
        self.defn = defn
        self.hp = hp
        self.hp_max = hp
        self.exp = exp


class Character:
    def __init__(self) -> None:
        self.x = -1
        self.y = -1
        self.hp_max = 20
        self.hp = 20
        self.att = 2
        self.defn = 2
        self.lv = 1
        self.exp = 0
        self.weapon = 0
        self.armor = 0
        self.accessories = []

    def set_character_roc(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, d: str, grid: list) -> None:
        directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
        nx, ny = self.x + directions[d][0], self.y + directions[d][1]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            return False
        if grid[nx][ny] == "#":
            return False

        self.set_character_roc(nx, ny)
        return True

    def battle(self, m: Monster, is_boss: bool) -> bool:
        my_turn = True
        battle_ing = 1
        if is_boss and "HU" in self.accessories:
            self.hp = self.hp_max

        while True:
            if my_turn:
                if battle_ing == 1 and "CO" in self.accessories:
                    bonus = 3 if "DX" in self.accessories else 2
                    m.hp -= max(1, (self.att + self.weapon) * bonus - m.defn)
                else:
                    m.hp -= max(1, (self.att + self.weapon) - m.defn)
                if m.hp <= 0:  # 승리 그 승리아님 ㅋㅋ
                    return True
            else:
                if is_boss and battle_ing == 2 and "HU" in self.accessories:
                    self.hp -= 0
                else:
                    self.hp -= max(1, m.att - (self.defn + self.armor))
                if self.hp <= 0:  # 사망
                    self.hp = 0
                    return False

            my_turn = not my_turn
            battle_ing += 1

    def exp_up(self, exp_point: int) -> None:
        if "EX" in self.accessories:
            exp_point = int(exp_point * 1.2)

        self.exp += exp_point
        if self.exp >= self.lv * 5:  # 레벨 업
            self.lv += 1
            self.exp = 0
            self.hp_max += 5
            self.hp = self.hp_max
            self.att += 2
            self.defn += 2

    def get_item(self, item: Item) -> None:
        item_type, value = item.item_type, item.value

        if item_type == "W":  # 무기
            self.weapon = int(value)
        elif item_type == "A":  # 방어구
            self.armor = int(value)
        else:  # 장신구
            if len(self.accessories) < 4 and value not in self.accessories:
                self.accessories.append(value)

    def heal_by_HR(self) -> None:
        if "HR" in self.accessories:
            self.hp = min(self.hp_max, self.hp + 3)

    def is_revived(self) -> bool:
        if "RE" in self.accessories:
            self.hp = self.hp_max
            self.accessories.remove("RE")
            return True

        return False

    def print_stat(self) -> None:
        print("LV : %d" % self.lv)
        print("HP : %d/%d" % (self.hp, self.hp_max))
        print("ATT : %d+%d" % (self.att, self.weapon))
        print("DEF : %d+%d" % (self.defn, self.armor))
        print("EXP : %d/%d" % (self.exp, self.lv * 5))


class Board:
    def __init__(self) -> None:
        self.grid = [list(input().rstrip()) for _ in range(N)]
        self.event_map = [[-1] * M for _ in range(N)]

    def print_map(self) -> None:
        for i in range(N):
            print("".join(self.grid[i]))


class RPG_Extreme:
    def __init__(self, N: int, M: int) -> None:
        self.turns = 0
        self.board = None  # 보드 객체
        self.player = None
        self.command = None  # 게임 커맨드
        self.monster_cnt = 0  # 몬스터
        self.monsters = []
        self.item_cnt = 0  # 아이템
        self.items = []
        self.sx = None  # 시작 지점(부활 위치)
        self.sy = None

    def init_game(self) -> None:
        self.board = Board()
        self.player = Character()
        self.command = input().rstrip()

        for i in range(N):
            for j in range(M):
                if self.board.grid[i][j] == "@":
                    self.player.set_character_roc(i, j)
                    self.board.grid[i][j] = "."
                    self.sx, self.sy = i, j
                elif self.board.grid[i][j] == "&" or self.board.grid[i][j] == "M":
                    self.monster_cnt += 1
                elif self.board.grid[i][j] == "B":
                    self.item_cnt += 1

        for i in range(self.monster_cnt):
            x, y, name, W, A, H, E = input().split()

            x, y = int(x) - 1, int(y) - 1
            self.monsters.append(Monster(name, int(W), int(A), int(H), int(E)))
            self.board.event_map[x][y] = i

        for i in range(self.item_cnt):
            x, y, item_type, value = input().split()

            x, y = int(x) - 1, int(y) - 1
            self.items.append(Item(item_type, value))
            self.board.event_map[x][y] = i

    def game_end(self, mark: bool) -> None:
        if mark:
            self.board.grid[self.player.x][self.player.y] = "@"
        self.board.print_map()
        print("Passed Turns : %d" % self.turns)
        self.player.print_stat()

    def run(self) -> str:
        for com in self.command:
            # 턴 시작
            self.turns += 1

            # 이동
            self.player.move(com, self.board.grid)

            # 이벤트 발생
            e = self.board.grid[self.player.x][self.player.y]
            if e == "B":
                idx = self.board.event_map[self.player.x][self.player.y]
                self.player.get_item(self.items[idx])
                self.board.grid[self.player.x][self.player.y] = "."
            elif e == "&" or e == "M":
                idx = self.board.event_map[self.player.x][self.player.y]
                is_boss = True if e == "M" else False

                # 졌다!
                if not self.player.battle(self.monsters[idx], is_boss):
                    if not self.player.is_revived():
                        self.game_end(False)
                        return "YOU HAVE BEEN KILLED BY %s.." % self.monsters[idx].name
                    self.player.set_character_roc(self.sx, self.sy)  # 부활후 리젠 장소
                    self.monsters[idx].hp = self.monsters[idx].hp_max  # 몬스터도 부활함
                    continue
                # 이겼다!
                self.player.exp_up(self.monsters[idx].exp)  # 경험치 획득
                self.player.heal_by_HR()  # 장신구에 의한 체력회복 없으면 안함
                self.board.grid[self.player.x][self.player.y] = "."  # 몬스터 삭제
                if is_boss:
                    self.game_end(True)
                    return "YOU WIN!"
            elif e == "^":
                damage = 1 if "DX" in self.player.accessories else 5
                self.player.hp -= damage
                if self.player.hp <= 0:  # 사망
                    if not self.player.is_revived():
                        self.game_end(False)
                        return "YOU HAVE BEEN KILLED BY SPIKE TRAP.."
                    # 악세서리 부활 이벤트
                    self.player.set_character_roc(self.sx, self.sy)
            else:
                pass

        self.game_end(True)
        return "Press any key to continue."


N, M = map(int, input().split())
game = RPG_Extreme(N, M)
game.init_game()
print(game.run())

"""
17081. RPG Extreme
    - 정신나감 ㅋㅋ
"""