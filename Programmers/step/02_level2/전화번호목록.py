def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        length = len(phone_book[i])

        if phone_book[i] == phone_book[i + 1][:length]:
            return False

    return True


phone_book = ["1195524421", "119", "97674223"]
print(solution(phone_book))


"""
lv2 전화번호 목록
    1. sorting 이후, i번째와 i + 1번째만 검사의 정당성
    - 파라미터로 주어지는 list의 원소가 문자열로 구성되어 있으므로,
      수의 크기가 아니라 사전순서로 sorting 한다. (이후 자동적으로 원소 문자열의 길이로 정렬함)

      긴 문자열이 짧은 문자열의 접두사가 될 수는 없으므로 뒷 쪽의 원소가 앞의 원소의 접두사가 될 수 없고, 
      사전순서대로 배열되는 결과로 i번째 원소가 i+1원소의 접두사가 아니라면 그 뒷쪽의 원소는 i번째 원소를 접두사로 절대 가질수 없게된다. 

      따라서 이 풀이법은 앞의 원소의 길이만큼만 검사하면서 넘어가면되고 O(n) 시간복잡도로 해결할 수 있다. 
    
    2. 문제의 태그가 hashmap인데,,
    - 1.의 풀이로 AC 받은 뒤에 hashmap으로 다시 풀이하려고 했는데, O(n^2)보다 작은 시간복잡도는 생각이 안난다.....

    3. 그냥 검사하는 방법
    - 이건 잠깐만 생각해봐도 O(n^2)을 가지므로 효율적인 풀이가 아니다.
"""