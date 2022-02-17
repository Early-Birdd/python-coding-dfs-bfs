from collections import deque

n, k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
         if graph[i][j] != 0:
             data.append((graph[i][j], 0, i, j))

data.sort() #바이러스 번호 순으로 정렬
q = deque(data)
s, x, y = map(int, input().split())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

while q:
    virus, cur_s, cur_x, cur_y = q.popleft()
    if cur_s == s:
        break
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, cur_s + 1, nx, ny))

print(graph[x - 1][y - 1]) #0,0 부터 시작했으므로 -1

#회고
#append시 괄호 개수 조심하기
#30라인에서 graph[nx][ny] == virus로 입력하여 오류가 발생했다. 사소한 실수를 항상 조심하자