#점수 계산
array = []

for _ in range(8):
    array.append(int(input()))
    
array_sort = sorted(array, reverse=True)

sum = sum(array_sort[:5])
print(sum)

result = []
for i in range(5):
    result.append(array.index(array_sort[i])+1)

for i in sorted(result):
    print(i, end=" ")
    
#카드
N = int(input())
r = dict()
for _ in range(N):
    n = int(input())
    if n in r:
        r[n] += 1
    else:
        r[n] = 1

sort_r = sorted(r.items(), key=lambda x: (-x[1], x[0]))
print(sort_r[0][0])

#두 수의 합
import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
array.sort()
find = int(input())

start = 0
end = N-1

cnt = 0
while start<end:
    if array[start] + array[end] == find:
        start +=1
        end -=1
        cnt +=1
    elif array[start] + array[end] > find:
        end -=1
    else:
        start +=1
        
print(cnt)