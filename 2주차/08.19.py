#점프왕 젤리
"""
이 문제의 핵심은 depth를 들어가며 내가 갈 수 있는 영역이 어디인지 파악하는 것이다.
갈 수 있는 방향은 오른쪽, 아래쪽이며 이 두 가지 경우의 수를 dfs bfs로 들어가면 문제가 풀린다.
"""
#dfs
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(graph, x, y, visited):
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if not visited[x][y]:
        visited[x][y] = 1
        point = graph[x][y]
        #오른쪽
        dfs(graph, x, y+point, visited)
        #아래
        dfs(graph, x+point, y, visited)
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dfs(graph, 0, 0, visited)

if visited[-1][-1] == 1:
    print("HaruHaru")
else:
    print("Hing")

#bfs
from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        point = graph[x][y]
        #오른쪽
        if 0 <= y+point < N and not visited[x][y+point]:
            q.append((x, y+point))
            visited[x][y+point] = 1
        
        #아래
        if 0 <= x+point < N and not visited[x+point][y]:
            q.append((x+point, y))
            visited[x+point][y] = 1
            
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

bfs(graph, 0, 0, visited)

if visited[-1][-1] == 1:
    print("HaruHaru")
else:
    print("Hing")