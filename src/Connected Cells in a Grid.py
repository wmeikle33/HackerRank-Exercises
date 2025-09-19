from collections import deque

def connectedCell(matrix):
    n, m = len(matrix), len(matrix[0])
    dirs = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc]
    visited = set()
    best = 0
        
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and (i,j) not in visited:
                q = deque([(i, j)])
                visited.add((i, j))
                size = 1
                while q:
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = dr + r, c + dc
                        if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == 1 and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
                            size += 1
                best = max(best, size)
    return best
