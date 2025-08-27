from collections import deque

def solution(maps):
    result = bfs(0, 0, maps)
    return -1 if result == 1 else result

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps):
    n, m = len(maps), len(maps[0])  # 행, 열 크기
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위 벗어나면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            # 벽이면 continue
            if maps[nx][ny] == 0:
                continue
            
            # 처음 방문한 길이면 거리 갱신
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    return maps[n-1][m-1]
