#뒤집기
"""
뒤집기 숫자 변화의 규칙을 찾아내는 것이 중요하다고 생각
숫자의 변화가 일어남에 따라서 아래와 같은 규칙을 가지고 있음
0 -> 0
1 -> 1
2 -> 1
3 -> 2
4 -> 2
5 -> 3
6 -> 3
...
(N+1) // 2
"""
S = input()

cnt = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        cnt+=1

print((cnt+1)//2)

#방 번호
"""
새로운 플라스틱 세트를 개봉하는 규칙이 중요하다고 생각
0~5, 7~8는 나오는 숫자의 개수가 곧 세트를 개봉하는 숫자가 됌
6, 9는 나오는 숫자의 개수 +1 //2가 곧 세트를 개봉하는 숫자가 됌
4 -> 2
5 -> 3
6 -> 3
7 -> 4
8 -> 4
...
(N+1)//2
"""
S = list(map(int, input()))

cnt = 1
array = [0] * 10
for i in S:
    if i in [6, 9]:
        array[6] +=1
        array[9] +=1
    else:
        array[i] += 1

array[6] = (array[6]+1)//2
array[9] = (array[9]+1)//2

print(max(array))