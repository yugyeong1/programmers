from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    result = dfs(0, 0, n, m, maps)
    
    if result == 1:
        result = -1
    
    
    return result

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, n, m, maps):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
                
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[n-1][m-1]
                
    