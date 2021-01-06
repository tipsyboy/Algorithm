def get_dart_score(dartResult):
    score_board = []
    score = [str(i) for i in range(0, 11)]
    bonus = ["S", "D", "T"]
    options = ["*", "#"]

    for dart in dartResult:
        if dart in score:
            if dart == "0" and score_board and score_board[-1] == 1:
                score_board.pop()
                score_board.append(10)
            else:
                score_board.append(int(dart))
        elif dart in bonus:
            if dart == "D":
                score_board[-1] **= 2
            elif dart == "T":
                score_board[-1] **= 3
        elif dart in options:
            if dart == "#":
                score_board[-1] *= -1
            elif dart == "*":
                score_board[-1] *= 2
                if len(score_board) > 1:
                    score_board[-2] *= 2

    print(sum(score_board))

    return sum(score_board)


get_dart_score("1S2D*3T")
get_dart_score("1D2S#10S")
get_dart_score("1D2S0T")
get_dart_score("1S*2T*3S")
get_dart_score("1D#2S*3S")
get_dart_score("1T2D3D#")
get_dart_score("1D2S3T*")
