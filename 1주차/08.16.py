#ATM
"""
걸리는 시간을 최소로 하기 위해서는 뒤에 사람들이 기다리는 시간을 최소로 해야한다.
이는 즉 인출을 하는데 걸리는 시간이 작은 사람 순서대로 이용하는 것이 올바르다.
"""
N = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0
mid = 0

for i in array:
    result += (mid + i)
    mid += i
print(result)

#안테나
"""
안테나로부터 모든 집까지의 거리가 최소가 되려면 안테나는 중간에 설치 되는것이 중요
안테나가 홀수 일 때는 중간 번호에 설치, 짝수 일 때는 중간 2개에서 낮은것에 설치(값이 같으면 작은 번호라고 조건이 있음)
"""
N = int(input())
array = list(map(int, input().split()))
array.sort()

mid_value = array[(N-1)//2]
print(mid_value)

#주식
"""
가장 큰 이익을 남기기 위해서는 주식을 구매해 최댓 값에서 판매하는 전략이다
max value를 찾아 해당 지점에 도착했을 때 매수 했던 주식을 매도 한 뒤, 그 이후에 max value를 갱신해
다시 매매하는 방식을 활용

1차 시도
list를 활용하여 매수한 주식 금액을 appned하여 차익을 계산 -> 시간 초과
max value를 활용하여 max_value - array[i] 값으로 계산 -> 시간초과

여기서 더 이상의 계산횟수를 줄이는 건 의미가 없다고 판단하였고, 문제는 내가 쓰고 있는 max() 임을 확신했다
max값은 팔아야 할 시점을 구하기 위해서 필요하다. 그래서 array를 꺼꾸러 올라가면 현재 내가 있는 값이 max라고
지정해도 되겠다고 생각했다. 더 큰 값이 나온다면 max value를 현재 값으로 수정하고 작은 값이 나오면 max 값이랑 현재 값의 차익을 더하면 된다
"""
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    array = list(map(int, input().split()))
    
    result = 0
    max_value = array[-1]
    for i in range(N-1, -1, -1):
        if array[i] > max_value:
            max_value = array[i]
        else:
            result += max_value - array[i]
    print(result)

#카드 합체 놀이
N, M = map(int, input().split())
S = list(map(int, input().split()))

for i in range(M):
    S.sort()
    
    value = S[0] + S[1]
    S[0] = value
    S[1] = value
    
print(sum(S))

#빙고
"""
index 메서드를 사용하기 위해서 빙고를 하나의 리스트로 나열한 뒤, //와 %로 x y를 구해주었다.
빙고를 체크할 때 행, 열로 빙고가 되는지 체크를 해야한다.
하지만 5x5에서 대각선에 있는 자리인 경우 대각선도 검사해야하므로 메서드를 만들어서 추가하였다.
"""
array = [[0]*5 for _ in range(5)]
bingo = []

for _ in range(5):
    bingo += list(map(int, input().split()))

def cross_check(x, y):
    c = 0
    if x == 2 and y == 2:
        #좌상단 -> 우하단
        if sum([array[i][i] for i in range(5)]) == 5:
            c+=1
        #좌하단 -> 우상단
        if sum([array[4-i][i] for i in range(5)]) == 5:
            c+=1
    #좌상단 -> 우하단
    elif x == y:
        if sum([array[i][i] for i in range(5)]) == 5:
            c+=1
    #좌하단 -> 우상단
    elif x+y == 4:
        if sum([array[4-i][i] for i in range(5)]) == 5:
            c+=1
    return c


line = 0
cnt = 0
f = False
for _ in range(5):
    S = list(map(int, input().split()))
    for i in S:
        #값 찾기
        idx = bingo.index(i)
        x = idx // 5
        y = idx % 5
        
        #값 채우기
        array[x][y] = 1
        
        #상하 좌우 검사
        if sum(array[x]) == 5:
            line +=1
        if sum([i[y] for i in array]) == 5:
            line +=1
        #대각선 검사
        if x == y or x+y == 4:
            line += cross_check(x, y)
            
        cnt+=1
        
        if line >= 3:
            print(cnt)
            f = True
            break
    if f:
        break

#자리배정
"""
4가지 방향으로 나아가면서 각 배열에 숫자를 채워 넣은 후, 그 값을 찾아 index를 출력한다.
"""
C, R = map(int, input().split())
K = int(input())

array = [[0] * R for _ in range(C)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
array[0][0] = 1
cnt = 2
while cnt < C*R:
    for i in range(4):
        while True:
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < C and 0 <= ny < R and array[nx][ny] == 0:
                array[nx][ny] = cnt
                cnt +=1
                x = nx
                y = ny
            else:
                break
if C*R < K:
    print(0)
else:
    for i in range(C):
        if K in array[i]:
            value = array[i].index(K)
            print(i+1, value+1)

#마인크래프트
"""
높이를 0 ~ max height 까지 시간을 구해가며 최솟값을 찾는다.
핵심은 설치를 할 블록의 개수가 주어진 블럭 + 파낸 블럭의 개수보다 작거나 같냐가 관건이다.
"""
N, M, B = map(int, input().split())
array = [list(map(int, input().split())) for i in range(N)]

area = dict()
for i in range(N):
    for j in range(M):
        if array[i][j] in area:
            area[array[i][j]] +=1
        else:
            area[array[i][j]] = 1

max_height = max(area.keys())

height = 0
time_zone = []
for i in range(max_height+1):
    time = 0
    block = B
    
    for k,v in area.items():
        if i < k:
            time += (k-i) * 2 * v
            block += (k-i) * v
        elif i > k:
            time += (i-k) * v
            block -= (i-k) * v
    
    if block >= 0:
        time_zone.append(time)
    else:
        time_zone.append(-1)
        
result_height = 0
result_time = max(time_zone)
for i in range(len(time_zone)):
    if time_zone[i] >= 0 and result_time >= time_zone[i]:
        result_height = i
        result_time = time_zone[i]
print(result_time, result_height)

#오목
"""
오목을 체크하는데는 총 4가지 방향을 체크 -> [우방향, 하방향, 우하단, 우상단]
오목은 아래 3가지를 충족해야 완료
1. 같은 돌이 5번 놓아져야 한다
2. 6번째 돌이 달라야한다(육목방지)
3. 이전 돌이 달라야한다(육목방지)
"""
import sys
input = sys.stdin.readline

array = [list(map(int, input().split())) for _ in range(19)]
find = False

dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]
for i in range(19):
    for j in range(19):
        if array[i][j] == 0:
            continue
        
        for k in range(4):
            cnt = 1
            nx = i+dx[k]
            ny = j+dy[k]
            
            while 0 <= nx < 19 and 0 <= ny < 19 and array[i][j] == array[nx][ny]:
                cnt +=1
                
                if cnt == 5:
                    #육목 체크
                    if 0 <= nx+dx[k] < 19 and 0 <= ny+dy[k] < 19 and array[i][j] == array[nx+dx[k]][ny+dy[k]]:
                        break
                    #이전 체크
                    if 0 <= i-dx[k] < 19 and 0 <= j-dy[k] < 19 and array[i][j] == array[i-dx[k]][j-dy[k]]:
                        break
                    
                    print(array[i][j])
                    print(i+1, j+1)
                    find = True
                    break
                
                nx += dx[k]
                ny += dy[k]
            
    if find:
        break
    
if not find:
    print(0)