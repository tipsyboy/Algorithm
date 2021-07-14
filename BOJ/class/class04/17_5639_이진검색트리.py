import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def pre_to_post(start, end):
    if start > end:  # 1) start index가 커지면 더 이상 탐색 x
        return

    root = pre_rst[start]

    # 2)
    if root > pre_rst[end]:
        pre_to_post(start + 1, end)
        print(root)
        return

    # 3) 현재 root node를 기준으로 왼쪽/오른쪽 노드 뭉치를 나누기 위해서 idx를 찾는다.
    idx = start + 1
    while idx <= end:
        if root < pre_rst[idx]:
            break
        idx += 1

    # 4) 후위 순회(postorder traversal)의 정의에 따라 왼쪽/오른쪽/루트 순으로 탐색한다.
    pre_to_post(start + 1, idx - 1)
    pre_to_post(idx, end)
    print(root)


# 5) 입력 방식이 독특함. 기억해두기
pre_rst = []
while True:
    try:
        pre_rst.append(int(input()))
    except:
        break

pre_to_post(0, len(pre_rst) - 1)


"""
17. 5639 이진 검색 트리 (Silver 1)
    - 이진 탐색과 매우 유사한 모양의 코드. 당연하다.

    - Tree 전체를 두고 보면 전위 순회(preorder) 방식은 'root -> 왼쪽 -> 오른쪽' 순서로 출력이 된다. 
      우리가 입력 받은 결과 값이 preorder의 방식의 결과물이므로 당연히 이 방식에 의해서 출력 되었을 것이고, 
      즉, 트리 전체의 첫 root인 첫 번째 값의 왼쪽 서브트리에는 root 보다 작은 값들이, 오른쪽 서브트리에는 root 보다 큰 값들이 저장되어 있다. 

      따라서, preorder의 결과 값을 [root / 왼쪽 서브 트리 / 오른쪽 서브 트리] 형식으로 나누고 후위 순회(postorder)에 맞춰서 재귀 호출한다.

      이때 나뉜 [왼쪽 서브 트리 / 오른쪽 서브 트리]는 그 자체로 다시 이진 검색 트리를 형성하므로 다시 [root / 왼쪽 서브 트리 / 오른쪽 서브 트리] 형태로
      재귀 호출해서 해결할 수 있다. 
    
    #######
    - 위 코드의 2)번의 내용은 현재 트리의 root 노드가 마지막 값보다 큰 경우, 뒤에 남은 값들은 전부 현재의 왼쪽 서브 트리를 의미하므로 
      idx를 찾는 과정 없이 호출하는 것인데, boj 결과로는 5000ms -> 80ms로 드라마틱하게 줄어들었다. 

      idx 탐색 과정이 완전 탐색이기 때문에 시간 복잡도가 줄겠거니 생각은 했으나, 이렇게 크게 줄어든 것에 대해서는 잘 모르겠다.....
"""
