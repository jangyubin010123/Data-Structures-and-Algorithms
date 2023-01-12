# <Q29> 공유기 설치

# my solution (X) -->> 다음에 다시 한 번 풀어볼 것..!!

# <A29> 공유기 설치
# 이 문제는 '가장 인접한 두 공유기 사이의 거리'의 최댓값을 탐색해야 하는 문제로 이해할 수 있다.
# -->> "이때 각 집의 좌표가 최대 10억(탐색 범위가 10억)이므로," -->> "이진 탐색을 이용하면 문제를 해결할 수 있다."
# -->> "따라서 이진 탐색으로 '가장 인접한 두 공유기 사이의 거리'를 조절해가며, 매 순간 실제로 공유기를 설치하여 C보다 많은 개수로 공유기를 설치할 수 있는지
# 체크하여 문제를 해결할 수 있다."
# 다만, '가장 인접한 두 공유기 사이의 거리'의 최댓값을 찾아야 하므로, C보다 많은 개수로 공유기를 설치할 수 있다면 '가장 인접한 두 공유기 사이의 거리'의 값을 증가시켜서, -->> 더 큰 값에 대해서도 성립하는지 체크하기 위해 다시 탐색을 수행한다.
# 이 문제는 7장에서 다룬 "떡볶이 떡 만들기" 문제와 유사하게 이진 탐색을 이용해 해결할 수 있는 파라메트릭 서치 유형의 문제로 이해할 수 있다.
# 예를 들어 5개의 집이 있고, 각 좌표를 담은 수열이 [1, 2, 4, 8, 9]와 같다고 해보자.
# 또한 설치할 공유기의 최소 개수 C = 3이라고 하자. 이때 가장 인접한 두 공유기 사이의 거리(gap)는 1부터 8까지의 수가 될 수 있다.
# * 최대 gap : 8 # -->> array[-1] - array[0] (단, 오름차순 정렬 기준입니다..!!)
# * 최소 gap : 1
# <step 1> 범위가 1부터 8까지이므로, gap의 값을 중간에 해당하는 4로 설정한다. 다만, 이 경우, 공유기를 2개 밖에 설치할 수 없다. 따라서 C = 3보다 작기 때문에, gap을 더 줄일 필요가 있다.
# 따라서 범위가 [1, 8]이었으므로, 범위를 [1, 3]으로 수정한다. (공유기를 앞에서 부터 차례대로 설치할 때, 공유기가 설치되는 위치는 하늘색으로 색칠하였다.)
# * 최대 gap : 8
# * 최소 gap : 1    gap = 4 ....
# <step 2> 범위가 1부터 3이므로, gap의 값을 중간에 해당하는 2로 설정한다. 이 경우, 공유기를 3개 설치하게 된다. 따라서 C = 3 이상의 값이기 때문에, -->> 현재의 gap을 저장한 뒤에 gap의 값을 증가시켜서
# -->> gap의 값이 더 커졌을 때도 가능한지 확인할 필요가 있다. -->> 따라서 범위가 [1, 3]인 상태에서 범위를 [3, 3]으로 설정한다.
# * 최대 gap : 3
# * 최소 gap : 1    gap = 2 ....
# <step 3> 범위가 3부터 3까지이므로, gap의 값을 중간에 해당하는 3으로 설정한다. 이 경우, 공유기를 3개 설치하게 된다.
# 따라서 C = 3 이상의 값이기 때문에, -->> 현재의 gap을 저장한 뒤에 gap의 값을 증가시켜서 gap이 더 커졌을 때도 가능한지 확인할 필요가 있다.
# -->> 하지만 현재의 범위가 [3, 3]이므로, -->> 더 이상 범위를 변경할 수 없다.
# -->> "따라서 gap = 3이 최적의 경우이다."
# * 최대 gap : 3
# * 최소 gap : 3    gap = 3 ....
# -->> 이러한 과정을 소스코드로 담으면 다음과 같다.

# A29 답안 예시
"""
# 집의 개수(N)와 공유기의 개수(C)를 입력받기
n, c = list(map(int, input().split()))

# 전체 집의 좌표 정보를 입력받기
array = []
for _ in range(0, n):
    array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while start <= end:
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    value = array[0]
    count = 1
    # 현재의 mid 값을 이용해 공유기를 설치
    for i in range(1, n): # 앞에서부터 차근차근 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장 # <<-- 다음 번에 안될 상황을 대비해 그때그때마다 저장해주는 것입니다..!!
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)
"""
