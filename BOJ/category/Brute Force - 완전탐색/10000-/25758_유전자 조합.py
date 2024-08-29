# 2024.08.25 SUN
# https://www.acmicpc.net/problem/25758

import sys

input = sys.stdin.readline

N = int(input())
genes = list(input().split())

genes_dict = dict()
for gene in genes:
    genes_dict[gene] = genes_dict.get(gene, 0) + 1

ans = set()
for gen1 in genes_dict.keys():
    for gen2 in genes_dict.keys():
        if gen1 == gen2 and genes_dict[gen1] < 2:
            continue

        new_gene = gen1[0] + gen2[1]
        ans.add(chr(max(ord(new_gene[0]), ord(new_gene[1]))))

print(len(ans))
print(*sorted(ans))
