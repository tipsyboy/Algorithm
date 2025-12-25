# 2025.03.13 THU
# https://www.acmicpc.net/problem/4836

import sys

input = sys.stdin.readline


def check(dance):
    dl = dance.split()
    errors = set([5])
    condition3 = [False, False]

    dip_check = []
    for i in range(len(dl)):
        if dl[i] == "dip":
            if 5 in errors:
                errors.remove(5)

            if not (
                (i > 0 and dl[i - 1] == "jiggle")
                or (i > 1 and dl[i - 2] == "jiggle")
                or (i < len(dl) - 1 and dl[i + 1] == "twirl")
            ):
                dip_check.append(i)
                errors.add(1)

        if dl[i] == "twirl":
            condition3[0] = True

        if dl[i] == "hop":
            condition3[1] = True

    if not (len(dl) > 2 and dl[-3] == dl[-1] == "clap" and dl[-2] == "stomp"):
        errors.add(2)

    if condition3[0] and not condition3[1]:
        errors.add(3)

    if dl[0] == "jiggle":
        errors.add(4)

    for p in dip_check:
        dl[p] = "DIP"

    return errors, " ".join(dl)


while True:
    dance = input().rstrip()

    if dance == "":
        break

    errors, dance_rst = check(dance)

    if not errors:
        print("form ok:", dance_rst)
    elif len(errors) == 1:
        num = list(errors)[0]
        print(f"form error {num}:", dance_rst)
    else:
        sorted_errors = sorted(errors)
        form = "form errors " + ", ".join(map(str, sorted_errors[:-1])) + " and " + str(sorted_errors[-1]) + ":"
        print(form, dance_rst)
