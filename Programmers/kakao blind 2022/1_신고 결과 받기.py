# 1)
def solution1(id_list, report, k):
    report_dict = dict()
    get_mail = dict()
    for idv in id_list:
        get_mail[idv] = 0
        report_dict[idv] = set()

    for r in report:
        r_ter, r_ted = r.split()

        report_dict[r_ted].add(r_ter)

    for reportee in report_dict.keys():
        if len(report_dict[reportee]) < k:
            continue

        for reporter in report_dict[reportee]:
            get_mail[reporter] += 1

    rst = []
    for idv in id_list:
        rst.append(get_mail[idv])

    return rst


# 2)
def solution2(id_list, report, k):
    report = set(report)
    reported = dict()
    reporter = dict()
    for idv in id_list:
        reported[idv] = 0
        reporter[idv] = 0

    for r in report:
        reported[r.split()[1]] += 1

    for r in report:
        rt, ed = r.split()
        if reported[ed] < k:
            continue

        reporter[rt] += 1

    rst = []
    for idv in id_list:
        rst.append(reporter[idv])

    return rst


"""
    1. sol1 제출하고 다른 사람의 코드를 보니 report를 set()으로 바꿔 중복 리포트를 아예 제거하여 처리함. 
       
    2. 좋은 생각인거 같아서 채용하고 sol2 작성 (index() 함수로 rst를 구성하는 아이디어는 시간 손해 볼게 뻔하므로 버림)
    
    3. 처리할 report의 수가 줄었을테니 시간상 이득을 볼거라고 생각했는데, 
       list -> set 캐스팅이 시간을 잡아먹는지 sol1보다 더 느려졌다.
       (중복 리포팅이 없는 tc인듯..?)
"""