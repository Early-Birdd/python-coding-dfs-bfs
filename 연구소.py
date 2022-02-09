n, m = map(int, input().split())
data = []
after_wall = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def virus(i, j):
    for a in range(4):
        nx = i + dx[a]
        ny = j + dy[a]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if after_wall[nx][ny] == 0:
                after_wall[nx][ny] = 2
                virus(nx, ny)

def safe():
    safe_count = 0
    for i in range(n):
        for j in range(m):
            if after_wall[i][j] == 0:
                safe_count += 1

    return safe_count

def dfs(wall):
    global result #dfs를 반복하기 때문

    if wall == 3:
        for i in range(n):
            for j in range(m):
                after_wall[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if after_wall[i][j] == 2:
                    virus(i, j)

        result = max(result, safe())
        return result

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                wall += 1
                dfs(wall)
                data[i][j] = 0 #dfs로 n * m 만큼 하나씩 전부 돌면서 벽을 세워봐야 하기 때문에 초기화 작업이 필요하다
                wall -= 1

dfs(0)
print(result)
