def fail_rate(N, stages):
    users = len(stages)
    f_rate_dic = dict()

    for i in range(1, N + 1):
        # count()도 반복해서 했을 때, 눈에 띄는 속도차이 있음. 따라서 변수에 저장하는게 효율 더 좋음
        cnt = stages.count(i)

        if users == 0:
            f_rate_dic[i] = 0
            continue
        f_rate_dic[i] = cnt / users  # 실패율
        users -= cnt

    # dict를 sorted()에 그냥 넘겼을 때
    rst = sorted(f_rate_dic, key=lambda x: f_rate_dic[x], reverse=True)
    print(rst)
    return rst


fail_rate(5, [2, 1, 2, 6, 2, 4, 3, 3])  # [3,4,2,1,5]
fail_rate(4, [4, 4, 4, 4, 4])
fail_rate(5, [])
fail_rate(3, [1, 1, 1, 2, 2, 2, 2])
