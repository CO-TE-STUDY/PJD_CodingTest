#안전 영역
"""
최대 높이가 100인 영역에서 0~100까지 돌면서 생기는 안전 영역의 개수를 list에 담고 max값을 출력
"""
#dfs
import copy
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(array, x, y):
    array[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N:
            if array[nx][ny] > h:
                dfs(array, nx, ny)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

result = []
for h in range(100):
    array = copy.deepcopy(graph)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if array[i][j] > h:
                dfs(array, i, j)
                cnt +=1
    result.append(cnt)

print(max(result))

#bfs
from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(array, i, j):
    q = deque()
    q.append((i,j))
    array[i][j] = 0
    
    while q:
        i, j = q.popleft()
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0 <= nx < N and 0 <= ny < N:
                if array[nx][ny] > h:
                    q.append((nx, ny))
                    array[nx][ny] = 0

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

answer = []
for h in range(100):
    array = copy.deepcopy(graph)
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if array[i][j] > h:
                bfs(array, i, j)
                cnt+=1
                
    answer.append(cnt)
print(max(answer))

#숨바꼭질
#bfs
"""
bfs를 활용하여 -1, +1, *2의 경우의 수를 +1씩 값을 늘려주며 K index가 채워질때 까지 계산하면 된다고 생각
"""
from collections import deque
def bfs(array, start):
    array[start] = 1
    
    q  = deque()
    q.append(start)
    
    
    while q:
        if array[K] != 0:
            break
        x = q.popleft()
        x1 = x - 1
        x2 = x + 1
        x3 = x * 2
                
        if 0 <= x1 < 100001 and array[x1] == 0:
            array[x1] = array[x]+1
            q.append(x1)
        if 0 <= x2 < 100001 and array[x2] == 0:
            array[x2] = array[x]+1
            q.append(x2)
        if 0 <= x3 < 100001 and array[x3] == 0:
            array[x3] = array[x]+1
            q.append(x3)
            
N, K = map(int, input().split())
if abs(N - K) < 2:
    print(abs(N-K))
else:
    array = [0] * 100001
    bfs(array, N)
    print(array[K]-1)