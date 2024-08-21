###도시와 비트코인
#dfs
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(graph, x, y, visited):
    if x < 0 or x >= N or y < 0 or y >= M:
        return
    
    if graph[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        #오른쪽
        dfs(graph, x, y+1, visited)
        #아래
        dfs(graph, x+1, y, visited)

    

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dfs(graph, 0, 0, visited)

if visited[-1][-1] == 1:
    print("Yes")
else:
    print("No")

#bfs
from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, x, y, visited):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        if 0 <= x < N and 0 <= y < M:
            if graph[x][y] == 1 and visited[x][y] == 0:
                visited[x][y] = 1
                q.append((x, y+1))
                q.append((x+1, y))

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

bfs(graph, 0, 0, visited)

if visited[-1][-1] == 1:
    print("Yes")
else:
    print("No")
    
###바이러스
#dfs
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = 1
    
    for x in graph[v]:
        if not visited[x]:
            dfs(graph, x, visited)

computer = int(input())
line = int(input())

graph = [[i] for i in range(computer+1)]
visited = [0] * (computer+1)
for _ in range(line):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    
dfs(graph, 1, visited)

print(sum(visited[2:]))

#bfs
from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    
    while q:
        v = q.popleft()
        
        for x in graph[v]:
            if not visited[x]:
                visited[x] = 1
                q.append(x)

computer = int(input())
line = int(input())

graph = [[i] for i in range(computer+1)]
visited = [0] * (computer+1)

for _ in range(line):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    
bfs(graph, 1, visited)
print(sum(visited[2:]))

###섬의 개수
#dfs
import sys
sys.setrecursionlimit(100000)
imput = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(array, x, y):
    array[x][y] = 0
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < h and 0 <= ny < w:
            if array[nx][ny] == 1:
                dfs(array, nx, ny)

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    array = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0 
    for i in range(h):
        for j in range(w):
            if array[i][j] == 1:
                dfs(array, i, j)
                cnt +=1
    print(cnt)

#bfs
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(graph, x, y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    
while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt+=1
                
    print(cnt)