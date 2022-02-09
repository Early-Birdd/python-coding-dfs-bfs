from collections import deque

n, m, k, x = map(int, input().split()) #도시 개수, 도로 개수, 최단 거리, 출발 도시
go = [[] for _ in range(n + 1)] #도시의 인덱스가 필요

for _ in range(m):
    start, end = map(int, input().split())
    go[start].append(end)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for nx in go[now]:
        if distance[nx] == -1:
            distance[nx] = distance[now] + 1
            q.append(nx)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

#회고
#경로 설정 아이디어와 들린 곳을 체크하는 아이디어가 중요
#8번에서 .append를 하지 않고 바로 대입하여 오류 발생 -> [[], []] 형태이므로 바로 대입하면 [[], 값]이 된다
#19번에서 now를 x로 설정하여 오류 발생
#23번에서 range를 1부터 시작하지 않아 오류 발생
